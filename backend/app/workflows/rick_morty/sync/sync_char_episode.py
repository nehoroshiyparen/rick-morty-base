from ...base import BaseSyncWorkflow
from app.infrastructure.database import  BaseRepository

class CharacterEpisodeSyncWorkflow(BaseSyncWorkflow):
    def __init__(self, character_repo: BaseRepository, episode_repo: BaseRepository):
        super().__init__()
        self.character_repo = character_repo
        self.episode_repo = episode_repo

    async def _prepare_data(self, mapped_data):
        char_ext_ids = set()
        episode_ext_ids = set()

        for item in mapped_data:
            episode_ext_ids.add(item["entity"].external_id)
            char_ext_ids.update(item["relations"]["characters"])
        
        characters = await self.character_repo.get_by_external_ids(list(char_ext_ids))
        episodes = await self.episode_repo.get_by_external_ids(list(episode_ext_ids))

        char_map = {c.external_id: c.id for c in characters}
        episode_map = {e.external_id: e.id for e in episodes}

        links = []

        for item in mapped_data:
            episode_ext_id = item["entity"].external_id
            episode_id = episode_map.get(episode_ext_id)

            if not episode_id:
                self.logger.warning(f"Episode not found: external_id={episode_ext_id}")
                continue

            for char_ext_id in item["relations"]["characters"]:
                char_id = char_map.get(char_ext_id)

                if not char_id:
                    self.logger.warning(
                        f"Character not found: external_id={char_ext_id}"
                    )
                    continue

                links.append((char_id, episode_id))

        return links

    async def _save(self, links: list):
        repo = self.character_repo.bind(self.session)
        await repo.add_episode_links_batch(links)