
GET_CENTRO = "SELECT codigocead as id,nombrecead as descripcion FROM soca2015.referencia_centro where codigocead= %s"

GET_CURSO = "SELECT consecutivo as id, mat_descripcion as descripcion from thumano20.materias where mat_pro = 32 and consecutivo= %s"

GET_PERIODO = "SELECT consecutivo as id,descripcion FROM thumano20.periodos where consecutivo= %s"

GET_PERIODO_ALL = "SELECT consecutivo as id,descripcion FROM thumano20.periodos where consecutivo=1701 or consecutivo=1704"

GET_ALL_LABORATORIO_CURSO_PERIODO = """
          SELECT
                lc.id,
                lc.curso AS id_curso,
                ac.mat_descripcion as descripcion,
                lc.centro ,
                rc.nombrecead,
                rz.nombre_zona,
                lc.estudiantes_grupo, 
                lc.horas_grupo, 
                lc.tipo_laboratorio, 
                lc.ubicacion, 
                lc.recurso   
                FROM
                soca2023.laboratorios_cursos_centro lc
                JOIN  thumano20.materias ac  ON lc.curso = ac.consecutivo
                JOIN soca2023.referencia_centro rc ON lc.centro = rc.codigocead
                JOIN soca2015.referencia_zona rz ON rc.zona = rz.codigo_zona
                WHERE
                periodo = %s;

            """


""" SELECT
                lc.id,
                lc.curso AS id_curso,
                ac.mat_descripcion as descripcion,
                lc.centro ,
                rc.nombrecead,
                rz.nombre_zona,
                lc.estudiantes_grupo, 
                lc.horas_grupo, 
                lc.tipo_laboratorio, 
                lc.ubicacion, 
                lc.recurso   
                FROM
                soca2023.laboratorios_cursos_centro lc
                JOIN  thumano20.materias ac  ON lc.curso = ac.consecutivo
                JOIN soca2023.referencia_centro rc ON lc.centro = rc.codigocead
                JOIN soca2015.referencia_zona rz ON rc.zona = rz.codigo_zona
                WHERE
                periodo=1701 """

GET_ALL_LABORATORIO_CURSO_PERIODO_CENTRO_NODO = """ 

                
            
SELECT
	R.id,
    R.curso,
    C.mat_descripcion as descripcion,
    R.centro,
    Ce.nombrecead AS nombre_centro_principal,
    R.centro_atender,
    Ca.nombrecead AS nombre_centro_atendido,
    R.estudiantes,
    R.horas,
    R.periodo
FROM 
    soca2023.laboratorios_cursos_nocentro R
JOIN 
    thumano20.materias C ON R.curso = C.consecutivo
JOIN 
    soca2015.referencia_centro Ce ON R.centro = Ce.codigocead
JOIN 
    soca2015.referencia_centro Ca ON R.centro_atender = Ca.codigocead
where R.periodo= %s;


                """



""" 
[

{
    idcurso:123
    nombre_curso:"curso",
    id_centro_ppal:"centro ppal"
    atiende:[
        {
            idcentro:456
            nombrecentro:"Centro 1"
        }
         {
            idcentro:456
            nombrecentro:"Centro 2"
        }
    ]
},

{
    idcurso:123
    nombre_curso:"curso",
    id_centro_ppal:"centro ppal"
    atiende:[
        {
            idcentro:456
            nombrecentro:"Centro 1"
        }
         {
            idcentro:456
            nombrecentro:"Centro 2"
        }
    ]
},

]

 """



"""
            SELECT 
                lc.id,
                lc.curso AS id_curso,
                ac.curso_descripcion ,
                lc.centro ,
                rc.nombrecead ,
                lc.estudiantes_grupo, 
                lc.horas_grupo, 
                lc.tipo_laboratorio, 
                lc.ubicacion, 
                lc.recurso   
                    

                FROM 
                soca2023.laboratorios_cursos_centro lc,
                soca2023.aad_cursos ac,
                soca2023.referencia_centro rc


                WHERE 
                lc.curso = ac.curso_equivalente and
                lc.centro = rc.codigocead and 
                lc.periodo = %s;

            """






#laboratorio original
"""
           SELECT
                lc.id,
                lc.curso AS id_curso,
                ac.mat_descripcion as descripcion,
                lc.centro ,
                rc.nombrecead ,
                lc.estudiantes_grupo, 
                lc.horas_grupo, 
                lc.tipo_laboratorio, 
                lc.ubicacion, 
                lc.recurso   
                FROM
                soca2023.laboratorios_cursos_centro lc
                JOIN  thumano20.materias ac  ON lc.curso = ac.consecutivo
                JOIN soca2023.referencia_centro rc ON lc.centro = rc.codigocead
                WHERE
                periodo = %s;

            """