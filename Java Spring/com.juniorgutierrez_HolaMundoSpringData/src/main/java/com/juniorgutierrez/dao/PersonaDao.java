package com.juniorgutierrez.dao;

import com.juniorgutierrez.domain.Persona;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

/**
 *
 * @author jg2kpy https://github.com/jg2kpy https://juniorgutierrez.com/
 */

//@Repositor
public interface PersonaDao extends CrudRepository<Persona, Long>{ }
