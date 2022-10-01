package com.privatpractice.practice.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import com.privatpractice.practice.models.Employee;

import java.util.List;
import java.util.Optional;

public interface EmployeeRepo extends JpaRepository<Employee, Long>
{
	void deleteEmployeeById(Long id);
	List<Employee> findEmployeeByDepartmentCode(int dc);
	Optional<Employee> findEmployeeById(Long id);
}