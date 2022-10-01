package com.privatpractice.practice;

import com.privatpractice.practice.models.Employee;
import com.privatpractice.practice.repositories.EmployeeRepo;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;

import java.time.LocalDate;
import java.time.Month;
import java.util.UUID;

@SpringBootApplication
/*@ComponentScan(basePackages = "com.privatpractice.practice.controllers"
				+ "com.privatpractice.practice.services"
				+ "com.privatpractice.practice.config"
				+ "com.privatpractice.practice.models"
				+ "com.privatpractice.practice.repositories"
			)*/
public class PracticeApplication {

	public static void main(String[] args) {
		SpringApplication.run(PracticeApplication.class, args);
	}
}

