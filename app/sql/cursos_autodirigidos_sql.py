

GET_CURSO_AUTO_ALL = """ SELECT 
    c.id,
    c.periodo,
    c.curso,
    m.consecutivo,
    m.mat_descripcion,
    e.descripcion AS escuela_descripcion
FROM 
    soca2023.project_cursos_autodirigidos AS c
 JOIN thumano20.materias AS m ON c.curso=m.consecutivo
 JOIN thumano20.codigo_escuelas AS e ON m.codigo_escuela=e.codigo_escuela
 where periodo=%s """
