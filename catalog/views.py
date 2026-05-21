from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def contacts(request):
    context = {}

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print('Новая заявка:')
        print(f'Имя: {name}')
        print(f'Телефон: {phone}')
        print(f'Сообщение: {message}')

        context['success'] = 'Сообщение успешно отправлено!'

    return render(request, 'contacts.html', context)