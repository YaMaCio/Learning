package com.privatpractice.practice.models;

import javax.persistence.*;
import java.io.Serializable;

@Entity
@Table(name = "empl")
public class Employee implements Serializable
{
	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	@Column(nullable = false, updatable = false)
	private Long id;
	private String name;
	private String surname;
	private String jobTitle;
	private String employmentDate;
    private int departmentCode;
	private String employeeUUID;
	
	public Employee() {}
	
	public Employee(String name, String surname, String jobTitle, String employmentDate, int departmentCode, String employeeUUID)
	{
		this.name = name;
		this.surname = surname;
		this.jobTitle = jobTitle;
		this.employmentDate = employmentDate;
		this.departmentCode = departmentCode;
		this.employeeUUID = employeeUUID;
	}
	
	public Long getId() { return id; }
	public void setId(Long id) { this.id = id; }
	public String getName() { return name; }
	public void setName(String name) { this.name = name; }
	public String getSurname() { return surname; }
	public void setSurname(String surname) { this.surname = surname; }
	public String getJobTitle() { return jobTitle; }
	public void setJobTitle(String jobTitle) { this.jobTitle = jobTitle; }
	public String getEmploymentDate() { return employmentDate; }
	public void setEmployeeDate(String employmentDate) { this.employmentDate = employmentDate; }
    public int getDepartmentCode() { return departmentCode; }
	public void setDepartmentCode(int departmentCode) { this.departmentCode = departmentCode; }
	public String getEmployeeCode() { return employeeUUID; }
	public void setEmployeeCode(String employeeUUID) { this.employeeUUID = employeeUUID; }
	
	@Override
	public String toString()
	{
		return "Employee{" +
				"id=" + id +
				", name='" + name + '\'' +
				", surname='" + surname + '\'' +
				", jobTitle='" + jobTitle + '\'' +
				", employmentDate='" + employmentDate + '\'' +
				", departmentCode='" + departmentCode + '\'' +
				", employeeUUID='" + employeeUUID + '\'' +
				'}';
	}
}
