with KPIs AS (
SELECT
    f.food_id,
    f.food_group,
    n.nutrient_id
    from {{ ref('fct_food_nutrients')}} fn
INNER JOIN {{ ref('dim_food')}} f
    ON fn.food_id = f.food_id
INNER JOIN {{ ref('dim_nutrients')}} n
    ON fn.nutrient_id = n.nutrient_id
),

total AS (
SELECT
    COUNT (DISTINCT food_id) AS product_count,
    COUNT (DISTINCT food_group) AS group_count,
    COUNT (DISTINCT nutrient_id) AS nutrient_count
FROM KPIs
)

SELECT
    *
FROM total