import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-student-profile',
  template: `
    <div class="profile-container">
      <h2>Student Profile (Angular Reactive Form)</h2>
      <form [formGroup]="profileForm" (ngSubmit)="onSubmit()">
        
        <div class="form-group">
          <label for="name">Full Name:</label>
          <input id="name" type="text" formControlName="name" />
          <div *ngIf="profileForm.get('name')?.touched && profileForm.get('name')?.invalid" class="error">
            <small *ngIf="profileForm.get('name')?.errors?.['required']">Name is required.</small>
          </div>
        </div>

        <div class="form-group">
          <label for="email">Email Address:</label>
          <input id="email" type="email" formControlName="email" />
          <div *ngIf="profileForm.get('email')?.touched && profileForm.get('email')?.invalid" class="error">
            <small *ngIf="profileForm.get('email')?.errors?.['required']">Email is required.</small>
            <small *ngIf="profileForm.get('email')?.errors?.['email']">Enter a valid email address.</small>
          </div>
        </div>

        <div class="form-group">
          <label for="semester">Semester (1-8):</label>
          <input id="semester" type="number" formControlName="semester" />
          <div *ngIf="profileForm.get('semester')?.touched && profileForm.get('semester')?.invalid" class="error">
            <small *ngIf="profileForm.get('semester')?.errors?.['required']">Semester is required.</small>
            <small *ngIf="profileForm.get('semester')?.errors?.['min'] || profileForm.get('semester')?.errors?.['max']">
              Semester must be between 1 and 8.
            </small>
          </div>
        </div>

        <button type="submit" [disabled]="profileForm.invalid" class="btn-submit">Submit Profile</button>
      </form>
    </div>
  `
})
export class StudentProfileComponent implements OnInit {
  profileForm!: FormGroup;

  ngOnInit(): void {
    this.profileForm = new FormGroup({
      name: new FormControl('', [Validators.required]),
      email: new FormControl('', [Validators.required, Validators.email]),
      semester: new FormControl(1, [Validators.required, Validators.min(1), Validators.max(8)])
    });
  }

  onSubmit(): void {
    if (this.profileForm.valid) {
      console.log('Profile Form Submitted:', this.profileForm.value);
    }
  }
}
