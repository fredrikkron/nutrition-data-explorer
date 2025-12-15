WITH selected_nutrients AS (
    SELECT
        f.food_id,
        f.food_name,
        n.nutrient_name,
        fn.value,
        n.unit
    FROM {{ ref('fct_food_nutrients') }} fn
    JOIN {{ ref('dim_food') }} f ON fn.food_id = f.food_id
    JOIN {{ ref('dim_nutrients') }} n ON fn.nutrient_id = n.nutrient_id
    WHERE n.nutrient_name IN (
        'Protein','Fett, totalt','Kolhydrater, tillgängliga','Fibrer','Energi (kcal)',
        'Vitamin A','Vitamin C','Vitamin D','Vitamin E','Vitamin B12',
        'Kalcium, Ca','Järn, Fe','Magnesium, Mg','Zink, Zn','Kalium, K'
    )
)
SELECT *
FROM selected_nutrients
