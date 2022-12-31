package com.juniorgutierrez.HolaSpring;

import com.juniorgutierrez.domain.Persona;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
//import org.springframework.web.bind.annotation.RestController;

/**
 *
 * @author jg2kpy
 */
@Controller
@Slf4j
public class ControladorInicio {
    
    @Value("${index.saludo}")
    private String saludo;
    
    @GetMapping("/")
    public String inicio(Model model){
        var mensaje = "Hola Mundo con Thymeleaft";
        
        var persona = new Persona();
        persona.setNombre("Jose");
        persona.setApellido("Gutierrez");
        persona.setEmail("jlgutierrez2000@hotmail.com");
        persona.setTelefono("123");
        
        var persona2 = new Persona();
        persona2.setNombre("Piper");
        persona2.setApellido("Perri");
        persona2.setEmail("piperperri@hotmail.com");
        persona2.setTelefono("1234");
        
        //List<Persona> personas = new ArrayList();
        //personas.add(persona);
        //personas.add(persona2);
        
        var personas = Arrays.asList(persona, persona2);
        //List<Persona> personas = null;
        
        log.info("ejecutando el controlador Spring MVC");
        model.addAttribute("mensaje", mensaje);
        model.addAttribute("saludo", saludo);
        model.addAttribute("persona", persona);
        model.addAttribute("personas", personas);
        return "index";
    }
}
