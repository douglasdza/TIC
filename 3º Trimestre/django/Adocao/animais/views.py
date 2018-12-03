# Uma classe simples para exibir uma página simples
from django.views.generic import TemplateView
# Serve para páginas que só tem HTML e talvez alguma consulta
# para listar coisas do banco

# Importar os modelos
from .models import*

# Importar os métodos View para inserir, alterar e excluir
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Importar a View para listar classes
from django.views.generic.list import ListView

# Importar a função para gerar o endereço de nossas URLS inteiras
from django.urls import reverse_lazy

# Página inicial
class Index(TemplateView):
    # Define qual o arquivo HTML vai ser usado para exibir esta página
    template_name = "pagina_inicial.html" # deve estar na pasta templates


# Página de ajuda
class Ajuda(TemplateView):
    # Define qual o arquivo HTML vai ser usado para exibir esta página
    template_name = "ajuda.html" # deve estar na pasta templates

class Contato(TemplateView):
    template_name = 'contato.html'

class CidadeCreate(CreateView):
    # Identificar o modelo
    model = Cidade
    # Define para onde vai redirecionar depois de inserir
    success_url = reverse_lazy('index')
    # Define qual o template vai ser usados
    template_name = 'form.html'
    # Define quais campos vão estar no formulário
    fields = ['nome', 'estado']

class CidadeUpdate(UpdateView):
    model = Cidade
    sucess_url = reverse_lazy('listar-cidades')
    template_name = 'form.html'
    fields = ['nome', 'estado']

class CidadeDelete(DeleteView):
    model = Cidade
    sucess_url = reverse_lazy('listar-cidades')
    template_name = 'form_delete.html'

class CidadeList(ListView):
    model = Cidade
    template_name = 'cidade_list.html'

class PessoaCreate(CreateView):
    # Identificar o modelo
    model = Pessoa
    # Define para onde vai redirecionar depois de inserir
    success_url = reverse_lazy('index')
    # Define qual o template vai ser usados
    template_name = 'form.html'
    # Define quais campos vão estar no formulário
    fields = ['nome', 'email', 'nascimento', 'cidade']

class PessoaUpdate(UpdateView):
    model = Pessoa
    success_url = reverse_lazy('listar-pessoas')
    template_name = 'form.html'
    fields = ['nome', 'email', 'nascimento', 'cidade']

class PessoaDelete(DeleteView):
    model = Pessoa
    success_url = reverse_lazy('listar-pessoas')
    template_name = 'form_delete.html'

class PessoaList(ListView):
    model = Pessoa
template_name = 'pessoa_list.html'
