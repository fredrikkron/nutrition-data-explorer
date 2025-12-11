with D_vitamin AS (
    SELECT
        f.food_id,
        f.food_name,
        f.food_group,
        fn.value AS Vitamin_D_amount
    FROM {{ ref('fct_food_nutrients') }} fn
    JOIN {{ ref('dim_food') }} f
        ON fn.food_id = f.food_id
    JOIN {{ ref('dim_nutrients') }} n
        ON fn.nutrient_id = n.nutrient_id
    WHERE n.nutrient_name = 'Vitamin D' AND fn.value > 5
)

SELECT
    *
FROM
    D_vitamin