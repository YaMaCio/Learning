package com.privatpractice.practice.config;

import com.privatpractice.practice.models.Employee;
import com.privatpractice.practice.repositories.EmployeeRepo;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.time.LocalDate;
import java.time.Month;
import java.util.UUID;

@Configuration
public class EmployeeConfig {
    @Bean
    CommandLineRunner initDB(EmployeeRepo repo)
    {
        return(args) ->
        {
            repo.save(new Employee("Fedor",
                    "Baier",
                    "Manager",
                    LocalDate.of(2006, Month.FEBRUARY, 5).toString(),
                    1, UUID.randomUUID().toString()));
            repo.save(new Employee("Fedor",
                    "Baier",
                    "Manager",
                    LocalDate.of(2006, Month.FEBRUARY, 5).toString(),
                    2, UUID.randomUUID().toString()));
            repo.save(new Employee("Fedor",
                    "Baier",
                    "Manager",
                    LocalDate.of(2006, Month.FEBRUARY, 5).toString(),
                    3, UUID.randomUUID().toString()));
            repo.save(new Employee("Fedor",
                    "Baier",
                    "Manager",
                    LocalDate.of(2006, Month.FEBRUARY, 5).toString(),
                    4, UUID.randomUUID().toString()));
            repo.save(new Employee("Fedor",
                    "Baier",
                    "Manager",
                    LocalDate.of(2006, Month.FEBRUARY, 5).toString(),
                    5, UUID.randomUUID().toString()));
            repo.save(new Employee("Fedor",
                    "Baier",
                    "Manager",
                    LocalDate.of(2006, Month.FEBRUARY, 5).toString(),
                    6, UUID.randomUUID().toString()));
            repo.save(new Employee("Fedor",
                    "Baier",
                    "Manager",
                    LocalDate.of(2006, Month.FEBRUARY, 5).toString(),
                    7, UUID.randomUUID().toString()));
            repo.save(new Employee("Fedor",
                    "Baier",
                    "Manager",
                    LocalDate.of(2006, Month.FEBRUARY, 5).toString(),
                    8, UUID.randomUUID().toString()));
        };
    }
}
