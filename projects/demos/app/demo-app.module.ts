import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {
  NgbTabsetModule,
  NgbCollapseModule,
  NgbTooltipModule,
} from '@ng-bootstrap/ng-bootstrap';
import { Angulartics2Module } from 'angulartics2';
import { DragAndDropModule } from 'angular-draggable-droppable';
import { DemoAppComponent } from './demo-app.component';
import { DemoComponent as DefaultDemoComponent } from './demo-modules/planhub/component';
import { DemoModule as DefaultDemoModule } from './demo-modules/planhub/module';
import { TaskComponent } from './demo-modules/tasks/component';
import { TaskModule } from './demo-modules/tasks/module';
import { EmptyComponent } from './demo-modules/empty-component/component';
import { EmptyModule } from './demo-modules/empty-component/module';
import { CompanyComponent } from './demo-modules/company-home/component';
import { CompanyModule } from './demo-modules/company-home/module';
import { ProfileComponent } from './demo-modules/profile/component';
import { ProfileModule } from './demo-modules/profile/module';
import { environment } from '../environments/environment';
import { FormsModule } from '@angular/forms';
import { ClipboardModule } from 'ngx-clipboard';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [DemoAppComponent],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    FormsModule,
    NgbTabsetModule,
    NgbCollapseModule,
    NgbTooltipModule,
    DragAndDropModule,
    HttpClientModule,
    Angulartics2Module.forRoot({
      developerMode: !environment.production,
    }),
    ClipboardModule,
    DefaultDemoModule,
    TaskModule,
    EmptyModule,
    CompanyModule,
    ProfileModule,
    RouterModule.forRoot(
      [
        {
          path: 'planhub',
          component: DefaultDemoComponent,
          data: {
            label: 'Planhub App',
          },
        },
        {
          path: 'tasks',
          component: TaskComponent,
          data: {
            label: 'Tasks',
          },
        },
        {
          path: 'milestones',
          component: EmptyComponent,
          data: {
            label: 'Milestones',
          },
        },
        {
          path: '**',
          redirectTo: 'planhub',
        },
      ],
      {
        useHash: true,
      }
    ),
  ],
  bootstrap: [DemoAppComponent],
})
export class DemoAppModule {}
