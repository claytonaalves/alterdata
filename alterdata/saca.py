#coding: utf8
import StringIO

# Os campos alfabéticos e alfanuméricos devem ser alinhados à esquerda e
# preenchidos com brancos à direita, quando for o caso;

# Os campos numéricos devem ser alinhados à direita e preenchidos com zeros
# à esquerda, quando for o caso;

# Todos os dados alfabéticos e alfanuméricos devem ser informados com
# caracteres maiúsculos;

# Os caracteres de edição ou máscara (ponto, vírgula etc.), devem ser omitidos,
# exceto quando as notas fiscais forem separadas por “ / ”. 

class Campo:

    def __init__(self, nome, posicao, tamanho, tipo, valor):
        self.nome = nome
        self.posicao = posicao
        self.tamanho = tamanho
        self.tipo = tipo
        self.valor = valor

    def __str__(self):
        if type(self.tipo)==list:
            return self.valor

        if self.tipo=='N':
            format_str = "{{0:0{0}}}".format(self.tamanho)
            return format_str.format(self.valor)
        elif self.tipo=='A':
            format_str = "{{0:{0}}}".format(self.tamanho)
            return format_str.format(self.valor.upper())


class Registro(object):

    def __init__(self, nota):
        self.linha = StringIO.StringIO()

    def adiciona_campo(self, campo):
        while self.linha.pos < (campo.posicao-1):
            self.linha.write(' ')
        self.linha.write(campo)

    def __str__(self):
        return self.linha.getvalue()+'\n'


# No registro "tipo 1", os campos relativos a remetente e destinatário somente
# devem ser utilizados por empresas de transporte para cadastramento do
# destinatário ou remetente visando a geração do registro 71 do Sintegra.
class Registro01(Registro):

    def __init__(self, nota):
        super(Registro01, self).__init__(self) 

        self.adiciona_campo(Campo('Codigo da empresa', 1, 5, 'N', nota.codigo_empresa))
        self.adiciona_campo(Campo('Especie NF', 6, 5, 'A', nota.especie_nf))
        self.adiciona_campo(Campo('Serie NF', 11, 5, 'A', nota.serie_nf))
        self.adiciona_campo(Campo('Numero NF', 16, 13, 'A', nota.numero))
        #self.adiciona_campo(Campo('Codigo Fiscal', 29, 3, 'N', nota.codigo_fiscal))
        self.adiciona_campo(Campo('Data de Emissão (DDMMAA)', 32, 6, 'N', nota.data_emissao))
        self.adiciona_campo(Campo('Data de Entrada/Saída (DDMMAA)', 38, 6, 'N', nota.data_entrada_saida))
        #self.adiciona_campo(Campo('Código Contábil UM', 44, 5, 'A'))
        #self.adiciona_campo(Campo('Código Contábil DOIS', 49, 5, 'A'))
        #self.adiciona_campo(Campo('Código Contábil TRÊS', 54, 5, 'A'))
        self.adiciona_campo(Campo('Código ou CNPJ do Fornecedor ou Cliente', 59, 16, 'N', nota.cnpj_cliente))
        self.adiciona_campo(Campo('Nome', 75, 40, 'A', nota.nome_cliente))
        self.adiciona_campo(Campo('Endereço', 115, 40, 'A', nota.endereco_cliente))
        self.adiciona_campo(Campo('Bairro', 155, 15, 'A', nota.bairro_cliente))
        self.adiciona_campo(Campo('Cidade', 170, 15, 'A', nota.cidade_cliente))
        self.adiciona_campo(Campo('CEP', 185, 8, 'N', nota.cep_cliente))
        self.adiciona_campo(Campo('UF', 193, 2, 'A', nota.uf_cliente))
        self.adiciona_campo(Campo('Telefone', 195, 12, 'A', nota.telefone_cliente))
        self.adiciona_campo(Campo('CNPJ/CPF', 207, 14, 'N', nota.cnpj_cliente))
        #self.adiciona_campo(Campo('Inscrição Estadual', 221, 16, 'A'))
        #self.adiciona_campo(Campo('Conta (código no plano de contas)', 237, 5, 'A'))
        self.adiciona_campo(Campo('Código da Natureza das operações', 242, 3, 'N', nota.cfop))
        self.adiciona_campo(Campo('Tipo da Nota: Entrada ou Saída', 245, 1, ['E', 'S'], nota.tipo))
        self.adiciona_campo(Campo('Registro Seqüencial para cada NF', 246, 6, 'N', nota.sequencial))
        #self.adiciona_campo(Campo('Cancelamento ou Exclusão de notas', 252, 1, 'C ou E'))
        self.adiciona_campo(Campo('Código Fiscal (usar para cfop de 4 digitos)', 253, 4, 'N', nota.cfop))
        #self.adiciona_campo(Campo('Conta (código no plano de contas)', 257, 10, 'A'))
        #self.adiciona_campo(Campo('Código Contábil QUATRO (st)', 267, 5, 'A'))
        #self.adiciona_campo(Campo('Código ou CNPJ do destinatário ou remente (*)', 272, 16, 'A'))
        #self.adiciona_campo(Campo('Nome do destinatário ou remetente (*)', 288, 40, 'A'))
        #self.adiciona_campo(Campo('Endereço do destinatário ou remetente (*)', 328, 40, 'A'))
        #self.adiciona_campo(Campo('Bairro do destinatário ou remetente (*)', 368, 15, 'A'))
        #self.adiciona_campo(Campo('Cidade do destinatário ou remetente (*)', 383, 15, 'A'))
        #self.adiciona_campo(Campo('CEP do destinatário ou remetente (*)', 398, 8, 'N'))
        #self.adiciona_campo(Campo('UF do destinatário ou remetente (*)', 406, 2, 'A'))
        #self.adiciona_campo(Campo('Telefone do destinatário ou remetente (*)', 408, 12, 'A'))
        #self.adiciona_campo(Campo('CNPJ/CPF do destinatário ou remetente (*)', 420, 14, 'N'))
        #self.adiciona_campo(Campo('Insc. Estadual do destinatário ou remetente (*)', 434, 16, 'A'))
        #self.adiciona_campo(Campo('Conta (código no plano de contas) do destinatário ou remetente (*)', 450, 5, 'A'))
        self.adiciona_campo(Campo('Código do País', 455, 5, 'N', nota.codigo_pais))
        #self.adiciona_campo(Campo('Inscrição Suframa', 460, 14, 'N'))
        self.adiciona_campo(Campo('Cód do município IBGE', 474, 7, 'N', nota.codigo_municipio_ibge))
        self.adiciona_campo(Campo('Código ou CNPJ do remetente', 481, 16, 'A', nota.cnpj_emitente))
        self.adiciona_campo(Campo('Nome do remetente', 497, 40, 'A', nota.nome_emitente))
        self.adiciona_campo(Campo('Endereço do remetente', 537, 40, 'A', nota.endereco_emitente))
        self.adiciona_campo(Campo('Bairro do remetente', 577, 15, 'A', nota.bairro_emitente))
        self.adiciona_campo(Campo('Cidade do remetente', 592, 15, 'A', nota.cidade_emitente))
        self.adiciona_campo(Campo('CEP do remetente', 607, 8, 'N', nota.cep_emitente))
        self.adiciona_campo(Campo('UF do remetente', 615, 2, 'A', nota.uf_emitente))
        self.adiciona_campo(Campo('Telefone do remetente', 617, 12, 'A', nota.telefone_emitente))
        self.adiciona_campo(Campo('CNPJ/CPF do remetente', 629, 14, 'N', int(nota.cnpj_emitente)))
        self.adiciona_campo(Campo('Insc. Estadual do remetente', 643, 16, 'A', nota.ie_emitente))
        #self.adiciona_campo(Campo('Conta (código no plano de contas) do remetente', 659, 5, 'A'))
        #self.adiciona_campo(Campo('Código ou CNPJ do consignatário', 664, 16, 'A'))
        #self.adiciona_campo(Campo('Nome do consignatário', 680, 40, 'A'))
        #self.adiciona_campo(Campo('Endereço do consignatário', 720, 40, 'A'))
        #self.adiciona_campo(Campo('Bairro do consignatário', 760, 15, 'A'))
        #self.adiciona_campo(Campo('Cidade do consignatário', 775, 15, 'A'))
        #self.adiciona_campo(Campo('CEP do consignatário', 790, 8, 'N'))
        #self.adiciona_campo(Campo('UF do consignatário', 798, 2, 'A'))
        #self.adiciona_campo(Campo('Telefone do consignatário', 800, 12, 'A'))
        #self.adiciona_campo(Campo('CNPJ/CPF do consignatário', 812, 14, 'N'))
        #self.adiciona_campo(Campo('Insc. Estadual do consignatário', 826, 16, 'A'))
        #self.adiciona_campo(Campo('Conta (código no plano de contas) do consignatário', 842, 5, 'A'))

        self.adiciona_campo(Campo('Campo para criar espaçamento', 842, 5, 'A', ' ')) # este campo não existe na documentação


class Registro02(Registro):

    def __init__(self, nota):
        super(Registro02, self).__init__(self)

        self.adiciona_campo(Campo('Observação da NF', 1, 250, 'A', ' '))

# 11. No Registro "tipo 3" as informações Base, Alíquota e Valor do Diferencial só
# devem ser preenchidas em códigos fiscais de Entrada, estes códigos devem
# ser configurados para calcular diferencial de alíquota igual a "Sim", no sistema
# de Escrita Fiscal Alterdata.

# 12. No Registro "tipo 3", as informações Ajuste ICMS e Ajuste IPI servem para
# identificar se os campos Valores de Ajuste do ICMS ou IPI serão negativos ou
# não, ou seja, se estes novos campos receberem "-", os valores serão negativos
# e se estiverem em branco, serão positivos.

# 13. Nos Registro "tipo 3", os campos "Código da embarcação" e "Descrição da
# embarcação" só devem ser informados para notas cujo campo Desoneração
# da Indústria Naval seja S (Sim).
class Registro03(Registro):

    def __init__(self, nota):
        super(Registro03, self).__init__(self)

        self.adiciona_campo(Campo('Valor Contábil', 1, 12, 'N', 0))
        self.adiciona_campo(Campo('ICMS Isentas', 13, 12, 'N', 0))
        self.adiciona_campo(Campo('ICMS Outras', 25, 12, 'N', 0))
        self.adiciona_campo(Campo('ICMS Base', 37, 12, 'N', 0))
        self.adiciona_campo(Campo('ICMS Alíquota', 49, 4, 'N', 0))
        self.adiciona_campo(Campo('ICMS Valor', 53, 12, 'N', 0))
        self.adiciona_campo(Campo('ICMS Ajuste', 65, 12, 'N', 0))
        self.adiciona_campo(Campo('IPI Isentas', 77, 12, 'N', 0))
        self.adiciona_campo(Campo('IPI Outras', 89, 12, 'N', 0))
        self.adiciona_campo(Campo('IPI Base', 101, 12, 'N', 0))
        self.adiciona_campo(Campo('IPI Alíquota', 113, 4, 'N', 0))
        self.adiciona_campo(Campo('IPI Valor', 117, 12, 'N', 0))
        self.adiciona_campo(Campo('IPI Ajuste', 129, 12, 'N', 0))
        self.adiciona_campo(Campo('Valor a abater da base de cal. PIS', 141, 12, 'N', 0))
        self.adiciona_campo(Campo('Valor a abater da base de cal. COFINS', 153, 12, 'N', 0))
        self.adiciona_campo(Campo('Base da Substituição tributária', 165, 12, 'N', 0))
        self.adiciona_campo(Campo('Valor da Substituição tributária', 177, 12, 'N', 0))
        self.adiciona_campo(Campo('Valor das Despesas Acessórias', 189, 12, 'N', 0))
        self.adiciona_campo(Campo('Código CIF_FOB (1=CIF, 2=FOB)', 201, 1, 'N', 0))
        self.adiciona_campo(Campo('Código de Modelo Fiscal', 202, 2, 'A', nota.modelo))
        #self.adiciona_campo(Campo('Identifica nota de Combustível (S/N)', 204, 204, 'A'))
        #self.adiciona_campo(Campo('Código Situação Tributária Federal', 205, 5, 'A'))
        #self.adiciona_campo(Campo('Cesta Básica (ES) (S/N)', 210, 1, 'A'))
        self.adiciona_campo(Campo('Base do Diferencial', 211, 13, 'N', 0))
        self.adiciona_campo(Campo('Alíquota do Diferencial', 224, 6, 'N', 0))
        self.adiciona_campo(Campo('Valor do Diferencial', 230, 13, 'N', 0))
        #self.adiciona_campo(Campo('Ajuste ICMS', 243, 1, 'A'))
        #self.adiciona_campo(Campo('Ajuste IPI', 244, 1, 'A'))
        #self.adiciona_campo(Campo('Código ECF', 245, 3, 'A'))
        #self.adiciona_campo(Campo('Contador Redução Z', 248, 6, 'N'))
        #self.adiciona_campo(Campo('Valor Total Inicial', 254, 12, 'N'))
        #self.adiciona_campo(Campo('Valor Total Final', 266, 12, 'N'))
        #self.adiciona_campo(Campo('Valor de venda (NF entrada)', 278, 12, 'N'))
        #self.adiciona_campo(Campo('Desoneração Industria Naval (RJ) (S/N)', 290, 1, 'A'))
        #self.adiciona_campo(Campo('Valor Cancelamento', 291, 12, 'N'))
        #self.adiciona_campo(Campo('Valor Descontos', 303, 12, 'N'))
        #self.adiciona_campo(Campo('Valor ISSQN', 315, 12, 'N'))
        #self.adiciona_campo(Campo('Valor Abatimento da base do IR', 327, 12, 'N'))
        #self.adiciona_campo(Campo('Valor Abatimento da base do CSLL', 339, 12, 'N'))
        #self.adiciona_campo(Campo('Status ICMS Antecipado', 351, 1, 'A'))
        #self.adiciona_campo(Campo('Status ICMS na Fonte', 352, 1, 'A'))
        #self.adiciona_campo(Campo('Status ICMS Valor Recolhido', 353, 1, 'A'))
        #self.adiciona_campo(Campo('Base ICMS interest.(Sub.Trib Interna RJ e GO)', 354, 12, 'N'))
        #self.adiciona_campo(Campo('Valor ICMS interest.  (Sub.Trib Interna RJ e GO)', 366, 12, 'N'))
        #self.adiciona_campo(Campo('ICMS Normal (GO)', 378, 12, 'N'))
        #self.adiciona_campo(Campo('Valor de venda Bruta', 390, 12, 'N'))
        #self.adiciona_campo(Campo('Contador de reinício', 402, 6, 'N'))
        #self.adiciona_campo(Campo('Valor do Frete', 408, 12, 'N'))
        #self.adiciona_campo(Campo('Valor do Seguro', 420, 12, 'N'))
        #self.adiciona_campo(Campo('Código da Embarcação (*)', 432, 4, 'N'))
        #self.adiciona_campo(Campo('Descrição da Embarcação', 436, 40, 'A'))
        #self.adiciona_campo(Campo('Alíquota FECP-RJ', 476, 6, 'A'))
        #self.adiciona_campo(Campo('Código Remetente', 482, 16, 'A'))
        #self.adiciona_campo(Campo('Código Destinatário', 498, 16, 'A'))
        #self.adiciona_campo(Campo('Tomador (R)emetente ou (D)estinatário ou (C) onsignatário', 514, 1, 'A'))
        #self.adiciona_campo(Campo('Data Emissão da Nota Fiscal atrelada ao CT', 515, 6, 'N'))
        #self.adiciona_campo(Campo('Modelo da Nota Fiscal atrelada ao CT', 521, 2, 'A'))
        #self.adiciona_campo(Campo('Série da Nota Fiscal atrelada ao CT', 523, 5, 'A'))
        #self.adiciona_campo(Campo('Número da Nota Fiscal atrelada ao CT', 528, 6, 'A'))
        #self.adiciona_campo(Campo('Valor Contábil da Nota Fiscal atrelada ao CT', 534, 12, 'N'))
        #self.adiciona_campo(Campo('Código da antecipação tributária (1a5 ou vazio)', 546, 1, 'A'))
        #self.adiciona_campo(Campo('Valor da Parcela Reduzida (GO)', 547, 12, 'N'))
        #self.adiciona_campo(Campo('Valor da Parcela Não Tributada (GO)', 559, 12, 'N'))
        #self.adiciona_campo(Campo('Número do caixa (DIEF CE)', 571, 4, 'N'))
        #self.adiciona_campo(Campo('Cód. Operação Doc. Fiscal (DIEF CE)', 575, 2, 'N'))
        #self.adiciona_campo(Campo('Cód. Situação Doc. Fiscal (DIEF CE)', 577, 2, 'N'))
        #self.adiciona_campo(Campo('Cód. Condição Participante (DIEF CE)', 579, 2, 'N'))
        #self.adiciona_campo(Campo('Cód. Motivo Referência Doc.  Fiscal (DIEF CE)', 581, 2, 'N'))
        #self.adiciona_campo(Campo('Cód. Número Segurança (DIEF CE)', 583, 2, 'N'))
        #self.adiciona_campo(Campo('Cód. Município (DIEF CE)', 585, 5, 'N'))
        #self.adiciona_campo(Campo('Descrição Município (DIEF CE)', 590, 50, 'A'))
        #self.adiciona_campo(Campo('UF Município (DIEF CE)', 640, 2, 'A'))
        #self.adiciona_campo(Campo('Subsérie da Nota (DIEF CE)', 642, 3, 'A'))
        #self.adiciona_campo(Campo('Número Dispositivo Segurança (DIEF CE)', 645, 10, 'A'))
        #self.adiciona_campo(Campo('Série Formulário (DIEF CE)', 655, 3, 'A'))
        #self.adiciona_campo(Campo('Subsérie Formulário (DIEF CE)', 658, 3, 'A'))
        #self.adiciona_campo(Campo('Número Inicial Formulário (DIEF CE)', 661, 10, 'A'))
        #self.adiciona_campo(Campo('Número Final Formulário (DIEF CE)', 671, 10, 'A'))
        #self.adiciona_campo(Campo('Valor Desconto Global (DIEF CE)', 681, 12, 'N'))
        #self.adiciona_campo(Campo('Valor Antecipado (DIEF CE)', 693, 12, 'N'))
        #self.adiciona_campo(Campo('ICMS Antecipado (DIEF CE)', 705, 12, 'N'))
        #self.adiciona_campo(Campo('Número Inicial Formulário (PI)', 717, 10, 'N'))
        #self.adiciona_campo(Campo('Número Final Formulário (PI)', 727, 10, 'N'))
        #self.adiciona_campo(Campo('Valor IPI não aproveitado', 737, 12, 'N'))
        #self.adiciona_campo(Campo('Número AIDF', 749, 20, 'A'))
        #self.adiciona_campo(Campo('Ano AIDF', 769, 4, 'N'))
        #self.adiciona_campo(Campo('Código de Situação do Documento', 773, 2, 'A'))
        self.adiciona_campo(Campo('Tipo de Pagamento', 775, 1, ['0', '1'], '0')) # 0 – à vista ou 1 – a prazo
        #self.adiciona_campo(Campo('Valor de Cancelamento do ISSQN', 776, 12, 'N'))
        #self.adiciona_campo(Campo('Valor de Cancelamento do ICMS', 788, 12, 'N'))
        #self.adiciona_campo(Campo('Valor de Desconto do ISSQN', 800, 12, 'N'))
        #self.adiciona_campo(Campo('Valor de Desconto do ICMS', 812, 12, 'N'))
        #self.adiciona_campo(Campo('Valor de Acréscimo do ISSQN', 824, 12, 'N'))
        #self.adiciona_campo(Campo('Valor de Acréscimo do ICMS', 836, 12, 'N'))
        #self.adiciona_campo(Campo('Código do Tipo de Receita (Simples Nacional)', 848, 3, 'A'))
        #self.adiciona_campo(Campo('Código Consignatário', 851, 16, 'A'))

        self.adiciona_campo(Campo('Campo para criar espaçamento', 851, 16, 'A', ' ')) # este campo não existe na documentação


class Registro04(Registro):

    def __init__(self, nota):
        super(Registro04, self).__init__(self)

        #self.adiciona_campo(Campo('Código de IPI (classificação fiscal - NBM/SH)', 1, 20, 'A'))
        #self.adiciona_campo(Campo('Unidade (KG,TN, M2,M3,etc.)', 21, 03, 'A'))
        #self.adiciona_campo(Campo('Quantidade (3 decimais)', 24, 10, 'N'))
        self.adiciona_campo(Campo('Valor Bruto (Quantidade x Valor Unitário)', 34, 12, 'N', int(round(nota.valor_total*100))))
        #self.adiciona_campo(Campo('Valor do IPI', 46, 10, 'N'))
        #self.adiciona_campo(Campo('Código situação tributária', 56, 03, 'N'))
        #self.adiciona_campo(Campo('Código do Produto', 59, 05, 'N'))
        #self.adiciona_campo(Campo('Base de Cálculo do ICMS Próprio', 64, 12, 'N'))
        #self.adiciona_campo(Campo('Base de Cálculo do ICMS Subst. Tributaria/ Base de ICMS Agregação (DIEF CE)', 76, 12, 'N'))
        #self.adiciona_campo(Campo('Vago', 88, 3, 'A'))
        #self.adiciona_campo(Campo('Desconto', 91, 12, 'N'))
        #self.adiciona_campo(Campo('Descrição do produto', 103, 35, 'A'))
        #self.adiciona_campo(Campo('Código Prodepe/Funcresce (PE)', 138, 3, 'N'))
        #self.adiciona_campo(Campo('Código Específico', 141, 14, 'A'))
        #self.adiciona_campo(Campo('Número Ordem Doc. Fiscal (COO)', 155, 6, 'N'))
        #self.adiciona_campo(Campo('Capacidade Volumétrica', 161, 5, 'N'))
        #self.adiciona_campo(Campo('Valor ICMS Próprio (DIEF CE)', 166, 12, 'N'))
        #self.adiciona_campo(Campo('Valor ICMS Agregação (DIEF CE)', 178, 12, 'N'))
        #self.adiciona_campo(Campo('Valor IPI Isentas (DIEF CE)', 190, 12, 'N'))
        #self.adiciona_campo(Campo('Valor IPI Outros (DIEF CE)', 202, 12, 'N'))
        #self.adiciona_campo(Campo('Qtd na Unidade Padrão (DIEF CE)', 214, 10, 'N'))
        #self.adiciona_campo(Campo('Valor Unitário na Unidade (DIEF CE)', 224, 12, 'N'))
        #self.adiciona_campo(Campo('Valor Unitário Bruto (DIEF CE)', 236, 12, 'N'))
        #self.adiciona_campo(Campo('Tipo de ICMS Agregação (DIEF CE)', 248, 2, 'N'))
        #self.adiciona_campo(Campo('Código do Valor Fiscal de ICMS (DIEF CE)', 250, 2, 'N'))
        #self.adiciona_campo(Campo('Código do Valor Fiscal de IPI (DIEF CE)', 252, 2, 'N'))
        #self.adiciona_campo(Campo('Base de IPI (DIEF CE)', 254, 12, 'N'))
        #self.adiciona_campo(Campo('Código Contábil do Produto (DIEF CE)', 266, 15, 'A'))
        #self.adiciona_campo(Campo('Descrição Contábil do Produto (DIEF CE)', 281, 50, 'A' ))

        self.adiciona_campo(Campo('Campo para criar espaçamento', 281, 50, 'A', ' ')) # este campo não existe na documentação

class Registro05(Registro):

    def __init__(self, nota):
        super(Registro05, self).__init__(self)

        #self.adiciona_campo(Campo('Identificador de nota de ISS (conteúdo = ISS)', 1, 3, 'A'))
        #self.adiciona_campo(Campo('Código da Empresa', 4, 5, 'N'))
        #self.adiciona_campo(Campo('Data (DDMMAA)', 9, 6, 'N'))
        #self.adiciona_campo(Campo('Número da Nota', 15, 12, 'A'))
        #self.adiciona_campo(Campo('Serie', 27, 5, 'A'))
        #self.adiciona_campo(Campo('Valor da Nota', 32, 12, 'N'))
        #self.adiciona_campo(Campo('Valor Isento da Nota', 44, 12, 'N'))
        #self.adiciona_campo(Campo('Alíquota do ISS', 56, 4, 'N'))
        #self.adiciona_campo(Campo('Valor do Imposto', 60, 12, 'N'))
        #self.adiciona_campo(Campo('Valor do Material (Empresas de São Paulo)', 72, 12, 'N'))
        #self.adiciona_campo(Campo('Valor base do serviço prestado por terceiros', 84, 12, 'N'))
        #self.adiciona_campo(Campo('Alíquota do Imposto de serviço de terceiros.', 96, 4, 'N'))
        #self.adiciona_campo(Campo('Valor do imposto retido do serviço de terceiros', 100, 12, 'N'))
        #self.adiciona_campo(Campo('Código Contábil do Cliente no Plano de Contas', 112, 5, 'A'))
        #self.adiciona_campo(Campo('Código do Lanç. Automático p/Valor da Nota', 117, 5, 'A'))
        #self.adiciona_campo(Campo('Código do Lanç. Automático p/Valor do ISS', 122, 5, 'A'))
        #self.adiciona_campo(Campo('Código do Lanç. Automático p/Valor do Material (SP)', 127, 5, 'A'))
        #self.adiciona_campo(Campo('Código do Lanç. Automático p/Valor de IRRF', 132, 5, 'A'))
        #self.adiciona_campo(Campo('Registro seqüencial', 137, 6, 'N')) #self.adiciona_campo(Campo('Código ou CNPJ do Cliente', 143, 16, 'N')) #self.adiciona_campo(Campo('Nome', 159, 40, 'A'))
        #self.adiciona_campo(Campo('Endereço', 199, 40, 'A'))
        #self.adiciona_campo(Campo('Bairro', 239, 15, 'A'))
        #self.adiciona_campo(Campo('Cidade', 254, 15, 'A'))
        #self.adiciona_campo(Campo('CEP', 269, 8, 'N'))
        #self.adiciona_campo(Campo('UF', 277, 278, 'A'))
        #self.adiciona_campo(Campo('Telefone', 279, 12, 'A'))
        #self.adiciona_campo(Campo('CNPJ/CPF', 291, 14, 'N'))
        #self.adiciona_campo(Campo('Inscrição Estadual', 305, 16, 'A'))
        #self.adiciona_campo(Campo('Conta (código no plano de contas)', 321, 10, 'A'))
        #self.adiciona_campo(Campo('Base Inss retido', 331, 12, 'N'))
        #self.adiciona_campo(Campo('Alíquota Inss retido', 343, 4, 'N'))
        #self.adiciona_campo(Campo('Valor Inss Retido', 347, 12, 'N'))
        #self.adiciona_campo(Campo('Valor de Dedução', 359, 12, 'N'))
        #self.adiciona_campo(Campo('Valor Iss Retido', 371, 12, 'N'))
        #self.adiciona_campo(Campo('Cancelamento 383', 383, 1 , 'C'))
        #self.adiciona_campo(Campo('Tipo Nota ou Recibo (vazio será Nota)', 384, 1, ['N', 'R']))
        #self.adiciona_campo(Campo('Código do Lanç. Automático p/Valor do PIS', 385, 5, 'A'))
        #self.adiciona_campo(Campo('Código do Lanç. Automático p/Valor do COFINS', 390, 5, 'A'))
        #self.adiciona_campo(Campo('Código do Lanç. Automático p/Valor do CSLL', 395, 5, 'A'))
        #self.adiciona_campo(Campo('Valor PIS Retido', 400, 12, 'N'))
        #self.adiciona_campo(Campo('Valor COFINS Retido', 412, 12, 'N'))
        #self.adiciona_campo(Campo('Valor CSLL Retido', 424, 12, 'N'))
        #self.adiciona_campo(Campo('Código do Serviço (SP)', 436, 4, 'N'))
        #self.adiciona_campo(Campo('Código do Lanç. Automático Subempreitada', 440, 5, 'A'))
        #self.adiciona_campo(Campo('Valor de Subempreitada', 445, 12, 'N'))
        #self.adiciona_campo(Campo('Código do Lanç. Automático ISS Retido', 457, 5, 'A'))
        #self.adiciona_campo(Campo('Código do Lanç. Automático INSS Retido', 462, 5, 'A'))
        #self.adiciona_campo(Campo('Código Modelo', 467, 5, 'A'))
        #self.adiciona_campo(Campo('Tipo Recolhimento', 472, 3, 'A'))
        #self.adiciona_campo(Campo('Número AIDF', 475, 20, 'A'))
        #self.adiciona_campo(Campo('Ano AIDF', 495, 4, 'N'))
        #self.adiciona_campo(Campo('Base Com Dedução 499 1', S, ou, 'N'))
        #self.adiciona_campo(Campo('Código de Operação', 500, 3, 'N'))
        #self.adiciona_campo(Campo('Status da Nota (DIEF RJ)', 503, 1, ['N', 'S', 'X']))
        #self.adiciona_campo(Campo('Número Inicial Formulário (DIEF RJ)', 504, 6, 'N'))
        #self.adiciona_campo(Campo('Número Final Formulário (DIEF RJ)', 510, 6, 'N'))
        #self.adiciona_campo(Campo('Data Extravio/Cancelamento (DIEF RJ) DDMMAAAA', 516, 8, 'N'))
        #self.adiciona_campo(Campo('Situação Nota Cancelada (DIEF RJ)', 524, 1, ['N', 'S', 'O']))
        #self.adiciona_campo(Campo('Valor Base (DIEF RJ)', 525, 12, 'N'))
        #self.adiciona_campo(Campo('Valor Isentas (DIEF RJ)', 537, 12, 'N'))
        #self.adiciona_campo(Campo('Valor Deduções (DIEF RJ)', 549, 12, 'N'))
        #self.adiciona_campo(Campo('Alíquota (DIEF RJ)', 561, 4, 'N'))
        #self.adiciona_campo(Campo('Valor ISS (DIEF RJ)', 565, 12, 'N'))
        #self.adiciona_campo(Campo('Valor ISS Retido (DIEF RJ)', 577, 12, 'N'))
        #self.adiciona_campo(Campo('Número Doc. Fiscal Substituído (DIEF RJ)', 589, 6, 'N'))
        #self.adiciona_campo(Campo('Motivo Cancelamento (DIEF RJ)', 595, 100, 'A'))
        #self.adiciona_campo(Campo('Código do Serviço (9 posições)', 695, 9, 'N'))
        #self.adiciona_campo(Campo('Base PIS Retido', 704, 12, 'N'))
        #self.adiciona_campo(Campo('Alíquota PIS Retido', 716, 4, 'N'))
        #self.adiciona_campo(Campo('Base COFINS Retido', 720, 12, 'N'))
        #self.adiciona_campo(Campo('Alíquota COFINS Retido', 732, 4, 'N'))
        #self.adiciona_campo(Campo('Base CSSL Retido', 736, 12, 'N'))
        #self.adiciona_campo(Campo('Alíquota CSSL Retido', 748, 4, 'N'))
        #self.adiciona_campo(Campo('Situação do documento', 752, 20, 'A'))
        #self.adiciona_campo(Campo('Nota fiscal eletrônica (NF-e)', 772, 1, ['N', 'S']))
        #self.adiciona_campo(Campo('Código de verificação (NF-e)', 773, 8, 'A'))
        #self.adiciona_campo(Campo('Discriminação do Serviço (NF-e)', 781, 255, 'A'))
        #self.adiciona_campo(Campo('Código de Situação do Documento', 1036, 2, 'A'))
        #self.adiciona_campo(Campo('Código Fiscal de Serviço', 1038, 4, 'A'))
        #self.adiciona_campo(Campo('Modelo da nota', 1042, 2, 'A'))
        #self.adiciona_campo(Campo('Subsérie', 1044, 5, 'A'))
        #self.adiciona_campo(Campo('Código do Município', 1049, 7, 'A'))
        #self.adiciona_campo(Campo('Código do País', 1056, 5, 'N'))
        #self.adiciona_campo(Campo('Inscrição Suframa', 1061, 14, 'N'))
        #self.adiciona_campo(Campo('Cód do município IBGE', 1075, 7, 'N'))
        #self.adiciona_campo(Campo('Código do Tipo de Receita (Simples Nacional)', 1082, 3, 'A'))

        self.adiciona_campo(Campo('Campo para criar espaçamento', 1082, 3, 'A', ' ')) # este campo não existe na documentação

class LayoutSACA:

    def __init__(self, nome_arquivo):
        self.arquivo = open(nome_arquivo, 'w')
        self.contador_notas = 0

    def adiciona_nota(self, nota):
        self.contador_notas += 1
        nota.sequencial = self.contador_notas 

        self.arquivo.write(str(Registro01(nota)))
        self.arquivo.write(str(Registro02(nota)))
        self.arquivo.write(str(Registro03(nota)))
        self.arquivo.write(str(Registro04(nota)))
        self.arquivo.write(str(Registro05(nota)))

    def grava(self):
        self.arquivo.close()

if __name__=="__main__":
    # arquivo = LayoutSACA('teste.saca')
    # arquivo.adiciona_nota(nota)
    # arquivo.adiciona_nota(nota)
    # arquivo.adiciona_nota(nota)
    # arquivo.grava()

    class Nota:
        pass

    nota = Nota()
    nota.codigo_empresa = 123
    nota.especie_nf = 'a'
    nota.serie_nf = '001'
    nota.codigo_fiscal = 2

    print Registro01(nota)

