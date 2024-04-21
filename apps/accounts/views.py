from django.views.generic import DetailView, UpdateView, CreateView
from django.db import transaction
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from .models import Profile
from .forms import UserUpdateForm, ProfileUpdateForm, UserRegisterForm, UserLoginForm



class UserRegisterView(SuccessMessageMixin, CreateView):
    """
    Представление для регистрации пользователя на сайте с формой регистрации
    """
    form_class = UserRegisterForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/user_register.html'
    success_message = 'Вы успешно зарегистрировались!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация пользователя'
        return context




class ProfileDetailView(DetailView):
    """
    Представление для просмотра профиля
    """
    model = Profile
    context_object_name = 'profile'
    template_name = 'accounts/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Профиль пользователя: {self.object.user.username}'
        return context


class ProfileUpdateView(UpdateView):
    """
    Представление для редактирования профиля
    """
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'accounts/profile_edit.html'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование профиля пользователя: {self.request.user.username}'
        if self.request.POST:
            context['user_form'] = UserUpdateForm(self.request.POST, instance=self.request.user)
        else:
            context['user_form'] = UserUpdateForm(instance=self.request.user)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        user_form = context['user_form']
        with transaction.atomic():
            if all([form.is_valid(), user_form.is_valid()]):
                user_form.save()
                form.save()
            else:
                context.update({'user_form': user_form})
                return self.render_to_response(context)
        return super(ProfileUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile_detail', kwargs={'slug': self.object.slug})
    

class UserLoginView(SuccessMessageMixin, LoginView):
    """
    Представление для авторизации пользователя на сайте
    """
    form_class = UserLoginForm
    template_name = 'accounts/user_login.html'
    next_page = 'home'
    success_message = 'Вы успешно вошли на сайт!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация пользователя'
        return context
    

class UserLogoutView(LogoutView):
    """
    Представление для выхода пользователя из системы
    """
    next_page = 'home'
    # template_name = 'accounts/user_logout.html'
    # success_message = 'Вы успешно вышли из системы!'