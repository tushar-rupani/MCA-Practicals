import { Component, OnInit } from '@angular/core';
import { Employee } from '../Employee';
import { EMPLOYEE } from '../employee-mock';
@Component({
  selector: 'app-employee',
  templateUrl: './employee.component.html',
  styleUrls: ['./employee.component.css']
})
export class EmployeeComponent implements OnInit {

  employees: Employee[] = EMPLOYEE;
  currentEmployee?: Employee;
  enableTxtBox = true;
  constructor() { }
  myClick(employee: Employee){
    this.currentEmployee = employee;
  }
  ngOnInit(): void {
  }

}
