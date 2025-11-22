with KPIs AS (
SELECT
    f.food_id,
    f.food_name,
    n.nutrient_name,
    fn.value
    from {{ ref('fct_food_nutrients')}} fn
INNER JOIN {{ ref('dim_food')}} f
    ON fn.food_id = f.food_id
INNER JOIN {{ ref('dim_nutrients')}} n
    ON fn.nutrient_id = n.nutrient_id
WHERE n.nutrient_name IN ('Protein') AND f.food_group != 'Rätter'
),

pivot_data AS (
SELECT
    food_id,
    food_name,
    MAX(value) AS protein_value
FROM KPIs
GROUP BY
    food_id,
    food_name
)

SELECT
    food_id,
    food_name,
    protein_value
FROM pivot_data
WHERE protein_value > 10.0
ORDER BY protein_value DESC