WITH carbs AS (
    SELECT
        f.food_id,
        f.food_name,
        f.food_group,
        n.nutrient_name,
        n.unit,
        fn.value
    FROM {{ ref('fct_food_nutrients') }} fn
    JOIN {{ ref('dim_food') }} f
        ON fn.food_id = f.food_id
    JOIN {{ ref('dim_nutrients') }} n
        ON fn.nutrient_id = n.nutrient_id
    WHERE f.food_name IN (
        'Potatis kokt m. salt',
        'Pommes frites friterad potatis fett ca 11% frysvara',
        'Ris basmati kokt m. salt',
        'Pasta kokt m. salt',
        'Bulgur kokt',
        'Couscous tillagad',
        'Nudlar äggnudlar kokta m. salt')
),

pivoted AS (
    SELECT
        food_name AS Livsmedel,
        MAX(CASE WHEN nutrient_name ILIKE '%Energi%' THEN value END) AS Kalorier_kcal,
        MAX(CASE WHEN nutrient_name ILIKE '%Kolhydrater, tillgängliga%' THEN value END) AS Kolhydrater_g,
        MAX(CASE WHEN nutrient_name ILIKE '%Protein%' THEN value END) AS Protein_g,
        MAX(CASE WHEN nutrient_name ILIKE '%Fett, totalt%' THEN value END) AS Fett_g,
        MAX(CASE WHEN nutrient_name ILIKE '%Fibrer%' THEN value END) AS Fibrer_g,
    FROM carbs
    GROUP BY Livsmedel
)

SELECT * 
FROM pivoted
ORDER BY Livsmedel