import { Component, OnInit } from '@angular/core';

@Component({
  templateUrl: './profile.component.html',
  styleUrls: ['./user-model.component.css']
})
export class ProfileComponent implements OnInit {

    name = 'abc xyz';
    mobile = "2385075847";
    email = "seriuvyi@shenrh";
    id = "iweu";
    category = "intern";
    firm_name = "-";

  constructor() { }

  ngOnInit(): void {
    /* get details and update em */
    console.log(this.name);
  }

}
