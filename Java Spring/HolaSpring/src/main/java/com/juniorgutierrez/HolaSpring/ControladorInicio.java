package com.juniorgutierrez.HolaSpring;

import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 *
 * @author jg2kpy
 */
@RestController
@Slf4j
public class ControladorInicio {
    
    @GetMapping("/")
    public String inicio(){
        log.info("ejecutando el controlador rest");
        log.debug("mas detalle del controlador");
        return "Hola Mundo con Spring";
    }
}
