CREATE TABLE meta (
  anometa smallint,
  mesmeta smallint,
  vendedorcodigo varchar(255),
  vendedornome varchar(255),
  valormeta double precision
);

/* INSERT INTO meta VALUES(?,?,?,?,?) */

select * from meta;

select 
    vendedorcodigo,
    vendedornome,
    sum(case when mesmeta = 'Janeiro' then valormeta end) as Janeiro,
    sum(case when mesmeta = 'Fevereiro' then valormeta end) as Fevereiro,
    sum(case when mesmeta = 'Março' then valormeta end) as Março,
    sum(case when mesmeta = 'Abril' then valormeta end) as Abril,
    sum(case when mesmeta = 'Maio' then valormeta end) as Maio,
    sum(case when mesmeta = 'Junho' then valormeta end) as Junho,
    sum(case when mesmeta = 'Julho' then valormeta end) as Julho,
    sum(case when mesmeta = 'Agosto' then valormeta end) as Agosto,
    sum(case when mesmeta = 'Setembro' then valormeta end) as Setembro,
    sum(case when mesmeta = 'Outubro' then valormeta end) as Outubro,
    sum(case when mesmeta = 'Novembro' then valormeta end) as Novembro,
    sum(case when mesmeta = 'Dezembro' then valormeta end) as Dezembro
from meta
group by vendedorcodigo, vendedornome;