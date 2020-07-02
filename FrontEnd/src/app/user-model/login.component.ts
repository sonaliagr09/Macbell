import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';


@Component({
  templateUrl: './login.component.html',
  styleUrls: ['./user-model.component.css']
})
export class LoginComponent implements OnInit {

    form: FormGroup;
    loading = false;
    submitted = false;

  constructor( 
    private formBuilder: FormBuilder
  ) { }

  ngOnInit(): void {
    this.form = this.formBuilder.group({
        email: ['', Validators.required],
        password: ['', [Validators.required, Validators.minLength(6)]],
    });
  }
  get f() { return this.form.controls; }

  onSubmit() {
    this.submitted = true;

    if (this.form.invalid) {
        console.log("form invalid");
        return;
    }
    else {
        console.log(this.form.value)
        /* Authentication from backend to be done here */
        
        /* Get User details from backend */

    }

}

}
