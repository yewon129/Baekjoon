SELECT ANIMAL_TYPE, IF(NAME IS NULL, 'No name', NAME) AS NAME, SEX_UPON_INTAKE 
FROM ANIMAL_INS;