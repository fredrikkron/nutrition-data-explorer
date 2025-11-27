with stg_livsmedel as (select * from {{ source('staging', 'data_Livsmedelsverket') }})

select
    nummer as food_id,
    namn as food_name,
    coalesce(gruppering, 'Övrigt') as food_group,
    naringsnamn as nutrient_name,
    enhet as unit,
    mangd as value
from
    stg_livsmedel
where unit NOT IN ('kJ', 'C22:5', 'C20:5', 'C22:6', 'NE/mg', 'skaletc.', 'RE/µg', '%')