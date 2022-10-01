package com.privatpractice.practice.controllers;

import com.privatpractice.practice.models.Employee;
import com.privatpractice.practice.repositories.EmployeeRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Map;

@Controller
public class MainController {
    @Autowired
    private EmployeeRepo employeeRepo;

    @GetMapping("/")
    public String homePage(Map<String, Object> model)
    {
        System.out.println("Redirect to home page");
        return "home";
    }

    @GetMapping("/login")
    public String loginForm(Map<String, Object> model)
    {
        return "login";
    }

    @GetMapping("/list")
    public String getEmployeeList (Map<String, Object> model)
    {
        List<Employee> employees = employeeRepo.findAll();
        Collections.sort(employees, new Comparator<Employee>()
        {
            @Override
            public int compare(Employee emp1, Employee emp2)
            {
                return emp1.getSurname().compareTo(emp2.getSurname());
            }
        });
        model.put("employeeList", employees);
        return "main";
    }

    @PostMapping("filter")
    public String filter(@RequestParam String dc, Map<String, Object> model)
    {
        List<Employee> emplList;
        if(dc != null && !dc.isEmpty()) {
            emplList = employeeRepo.findEmployeeByDepartmentCode(Integer.parseInt(dc));
        } else
        {
            emplList = employeeRepo.findAll();
        }
        Collections.sort(emplList, new Comparator<Employee>()
        {
            @Override
            public int compare(Employee emp1, Employee emp2)
            {
                return emp1.getSurname().compareTo(emp2.getSurname());
            }
        });
        model.put("employeeList", emplList);
        return "main";
    }

   /* @GetMapping("/l/{dc}")
    public String getAllEmployeesByDC(Map<String, Object> model, @PathVariable("dc") Long dc)
    {
        List<Employee> employees = employeeRepo.findAll();
        employees.removeIf(emp -> emp.getDepartmentCode() != dc);
        Collections.sort(employees, new Comparator<Employee>()
        {
            @Override
            public int compare(Employee emp1, Employee emp2)
            {
                return emp1.getSurname().compareTo(emp2.getSurname());
            }
        });
        model.put("employeeList", employees);
        return "main";
    }*/

}
