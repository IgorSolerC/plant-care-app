import { Routes } from '@angular/router';
import { LayoutComponent } from './shared/components/layout/layout.component';
import { LayoutEmptyComponent } from './shared/components/layout-empty/layout-empty.component';
import { HomeComponent } from './pages/home/home.component';
import { ExampleComponent } from './pages/example/example.component';
import { PageNotFoundComponent } from './pages/page-not-found/page-not-found.component';
import { AuthComponent } from './pages/auth/auth.component';
import { authGuard } from './core/guards/auth.guard';
import { ProfileComponent } from './pages/profile/profile.component';

export const routes: Routes = [
    {
        path: 'auth', component: LayoutEmptyComponent,
        children: [
            { path: '', component: AuthComponent, title: 'Auth' },
        ]
    },
    {
        path: '', component: LayoutComponent,
        children: [
            { path: '', redirectTo: '/home', pathMatch: 'full'},
            { path: 'home', component: HomeComponent, title: 'Início'},
            { path: 'example', component: ExampleComponent, title: 'Exemplo' },
            { path: 'profile', component: ProfileComponent, title: 'Profile'},
            { path: '**', component: PageNotFoundComponent, title: 'Página Não Encontrada'}
        ],
        canActivate: [authGuard]
    },
];  