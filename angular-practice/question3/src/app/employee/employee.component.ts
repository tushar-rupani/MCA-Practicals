import { Component, OnInit } from '@angular/core';
import { EMPLOYEE } from '../employee-mock';
import { Employee } from '../Employee';
@Component({
  selector: 'app-employee',
  templateUrl: './employee.component.html',
  styleUrls: ['./employee.component.css']
})
export class EmployeeComponent implements OnInit {

  employees: Employee[] = EMPLOYEE;
  constructor() { }

  ngOnInit(): void {
  }

}
