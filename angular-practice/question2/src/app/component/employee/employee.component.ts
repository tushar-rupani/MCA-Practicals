import { Component, OnInit } from '@angular/core';
import { Employee } from 'src/app/Employee';
import { EMPLOYEE } from 'src/app/employee-mock';
@Component({
  selector: 'app-employee',
  templateUrl: './employee.component.html',
  styleUrls: ['./employee.component.css']
})
export class EmployeeComponent implements OnInit {

  employee: Employee = EMPLOYEE;
  enableTxtBox = true;
  constructor() { }

  ngOnInit(): void {
  }
  nameChanged(value:any){
  }

}
