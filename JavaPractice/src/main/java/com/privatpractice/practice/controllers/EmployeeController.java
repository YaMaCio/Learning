package com.privatpractice.practice.controllers;

import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Map;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.privatpractice.practice.models.Employee;
import com.privatpractice.practice.services.EmployeeService;

@RestController
@RequestMapping("/employee")
public class EmployeeController
{
	private final EmployeeService employeeService;
	
	public EmployeeController(EmployeeService employeeService)
	{
		this.employeeService = employeeService;
	}


	
	@GetMapping("/all")
	public ResponseEntity<List<Employee> > getAllEmployees()
	{
		List<Employee> employees = employeeService.findAllEmployees();
		/*employees.removeIf(emp -> emp.getDepartmentCode() != dc);
		Collections.sort(employees, new Comparator<Employee>()
		{
			@Override
			public int compare(Employee emp1, Employee emp2)
			{
				return emp1.getSurname().compareTo(emp2.getSurname());
			}
		});*/
		return new ResponseEntity<>(employees, HttpStatus.OK);
	}
	
	@GetMapping("/find/{id}")
	public ResponseEntity<Employee> getEmployeeById(@PathVariable("id") Long id)
	{
		Employee employee = employeeService.findEmployeeById(id);
		return new ResponseEntity<>(employee, HttpStatus.OK);
	}
	
	@PostMapping("/add")
	public ResponseEntity<Employee> addEmployee(@RequestBody Employee employee)
	{
		Employee newEmployee = employeeService.addEmployee(employee);
		return new ResponseEntity<>(newEmployee, HttpStatus.CREATED);
	}
	
	@PutMapping("/update")
	public ResponseEntity<Employee> updateEmployee(@RequestBody Employee employee)
	{
		Employee updateEmployee = employeeService.updateEmployee(employee);
		return new ResponseEntity<>(updateEmployee, HttpStatus.OK);
	}
	
	@DeleteMapping("/delete/{id}")
	public ResponseEntity<Employee> deleteEmployee(@PathVariable("id") Long id)
	{
		employeeService.deleteEmployee(id);
		return new ResponseEntity<>(HttpStatus.OK);
	}
}