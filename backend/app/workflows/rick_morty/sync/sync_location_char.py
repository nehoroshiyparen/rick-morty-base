from ...base import BaseSyncWorkflow

class LocationCharacterSyncWorkflow(BaseSyncWorkflow):
    def __init__(self, location_repo, character_repo):
        super().__init__()
        self.character_repo = character_repo
        self.location_repo = location_repo

    async def _prepare_data(self, mapped_data):
        char_ext_ids = set()
        location_ext_ids = set()

        for item in mapped_data:
            char_ext_ids.add(item["entity"].external_id)
            location_ext_ids.add(item["relations"]["origin"])
            location_ext_ids.add(item["relations"]["location"])

        characters = await self.character_repo.get_by_external_ids(list(char_ext_ids))
        locations = await self.location_repo.get_by_external_ids(list(location_ext_ids))

        char_map = {c.external_id: c.id for c in characters}
        location_map = {l.external_id: l.id for l in locations}

        updates = []

        for item in mapped_data:
            char_id = char_map.get(item["entity"].external_id)
            if not char_id:
                self.logger.warning(
                    f"Character not found: external_id={item['entity'].external_id}"
                )
                continue

            location_ext_id = item["relations"]["location"]
            origin_ext_id = item["relations"]["origin"]

            location_id = location_map.get(location_ext_id)
            origin_id = location_map.get(origin_ext_id)

            updates.append((char_id, location_id, origin_id))

        return updates
            
    async def _save(self, updates):
        repo = self.character_repo.bind(self.session)
        await repo.update_locations(updates)