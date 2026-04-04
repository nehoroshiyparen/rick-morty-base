export interface Mapper<TDto, TDomain> {
  toDomain(dto: TDto): TDomain;
  toDto(domain: TDomain): TDto;
}
