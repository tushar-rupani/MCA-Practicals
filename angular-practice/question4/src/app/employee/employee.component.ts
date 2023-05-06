import { Component, OnInit } from '@angular/core';
import { Employee } from '../Employee';
import { EMPLOYEE } from '../employee-mock';
@Component({
  selector: 'app-employee',
  templateUrl: './employee.component.html',
  styleUrls: ['./employee.component.css']
})
export class EmployeeComponent implements OnInit {

  employee: Employee = EMPLOYEE;
  constructor() { }

  ngOnInit(): void {
  }

}
