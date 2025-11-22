with protein AS (
    SELECT
        f.food_id,
        f.food_name,
        f.food_group,
        n.nutrient_name,
        fn.value
    FROM {{ ref('fct_food_nutrients') }} fn
    JOIN {{ ref('dim_food') }} f
        ON fn.food_id = f.food_id
    JOIN {{ ref('dim_nutrients') }} n
        ON fn.nutrient_id = n.nutrient_id
    WHERE n.nutrient_name = 'Protein'
),

agg_group AS (
    SELECT
        food_group,
        round(avg(value), 1) AS avg_protein
    FROM protein
    GROUP BY food_group
)

SELECT *
FROM agg_group
ORDER BY avg_protein DESC
LIMIT 10