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
import { environment } from '../environments/environment';
import { FormsModule } from '@angular/forms';
import { ClipboardModule } from 'ngx-clipboard';

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
    Angulartics2Module.forRoot({
      developerMode: !environment.production,
    }),
    ClipboardModule,
    DefaultDemoModule,
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
