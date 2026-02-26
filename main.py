from flask import Flask, render_template, request

app = Flask(__name__)

# Dados dos relógios (Simulando um banco de dados)
RELOGIOS = [
    { 
        "id": 0,
        "nome": "The Heritage", 
        "sub": "Ouro Rosé 18k & Mostrador Onyx", 
        "preco": "R$ 320.000", 
        "img": "https://images.unsplash.com/photo-1612817159949-195b6eb9e31a?auto=format&fit=crop&q=80",
        "descricao": "O Heritage é a personificação da tradição clássica. Com uma caixa em ouro rosé 18k e um mostrador de ônix profundo, este relógio utiliza o Calibre C030 com 72 horas de reserva de marcha."
    },
    { 
        "id": 1,
        "nome": "The Astronomia", 
        "sub": "Platina & Complicação Lunar", 
        "preco": "R$ 485.000", 
        "img": "https://images.unsplash.com/photo-1547996160-81dfa63595aa?auto=format&fit=crop&q=80",
        "descricao": "Inspirado no cosmos, o Astronomia apresenta uma complicação de fase lunar de alta precisão em uma caixa de platina 950, protegida por um cristal de safira abaulado."
    },
    { 
        "id": 2,
        "nome": "The Skeleton", 
        "sub": "Cristal de Safira & Titânio Grau 5", 
        "preco": "R$ 550.000", 
        "img": "https://images.unsplash.com/photo-1587836171343-74d61901ddbf?auto=format&fit=crop&q=80",
        "descricao": "A transparência absoluta encontra a resistência extrema. O Skeleton revela cada engrenagem de seu movimento esqueleto, montado em uma estrutura de titânio de grau aeroespacial."
    },
    { 
        "id": 3,
        "nome": "The Tourbillon", 
        "sub": "Mecanismo Gravitacional & Ouro Branco", 
        "preco": "R$ 890.000", 
        "img": "https://images.unsplash.com/photo-1523170335258-f5ed11844a49?auto=format&fit=crop&q=80",
        "descricao": "A complicação suprema da relojoaria. O Tourbillon compensa os efeitos da gravidade para uma precisão absoluta, envolto em uma caixa elegante de ouro branco 18k."
    },
    { 
        "id": 4,
        "nome": "The Perpetual", 
        "sub": "Calendário Perpétuo & Couro de Jacaré", 
        "preco": "R$ 410.000", 
        "img": "https://images.unsplash.com/photo-1622434641406-a158123450f9?auto=format&fit=crop&q=80",
        "descricao": "Um relógio que entende o tempo através dos séculos. O Perpetual ajusta automaticamente a data, incluindo anos bissextos, até o ano 2100."
    },
    { 
        "id": 5,
        "nome": "The Vanguard", 
        "sub": "Carbono Forjado & Design Esportivo", 
        "preco": "R$ 275.000", 
        "img": "https://images.unsplash.com/photo-1524592094714-0f0654e20314?auto=format&fit=crop&q=80",
        "descricao": "Leveza e durabilidade incomparáveis. O Vanguard utiliza carbono forjado de alta tecnologia, resultando em um padrão único para cada peça produzida."
    },
    { 
        "id": 6,
        "nome": "The Abyss", 
        "sub": "Mergulho Profissional & Aço 904L", 
        "preco": "R$ 180.000", 
        "img": "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?auto=format&fit=crop&q=80",
        "descricao": "Projetado para as profundezas. O Abyss é resistente a 1000 metros de profundidade, com válvula de escape de hélio e luminescência de alta visibilidade."
    },
    { 
        "id": 7,
        "nome": "The Celestial", 
        "sub": "Mapa Estelar & Lápis-Lazúli", 
        "preco": "R$ 395.000", 
        "img": "https://images.unsplash.com/photo-1594534475808-b18fc33b045e?auto=format&fit=crop&q=80",
        "descricao": "Um pedaço do céu no seu pulso. O mostrador em pedra Lápis-Lazúli exibe a posição exata das constelações no hemisfério norte em tempo real."
    },
    { 
        "id": 8,
        "nome": "The Imperial", 
        "sub": "Platina & Diamantes Lapidação Baguette", 
        "preco": "R$ 1.250.000", 
        "img": "https://images.unsplash.com/photo-1604242692760-2f7b0c26856d?auto=format&fit=crop&q=80",
        "descricao": "O ápice do luxo BELMONT. O Imperial é cravejado com 48 diamantes de lapidação baguette e possui um mostrador em platina polida à mão."
    },
    { 
        "id": 9,
        "nome": "The Zenith", 
        "sub": "Ouro Rosé & Mostrador de Meteorito", 
        "preco": "R$ 620.000", 
        "img": "https://images.unsplash.com/photo-1548171915-e7af50a0af26?auto=format&fit=crop&q=80",
        "descricao": "Vindo do espaço sideral. O Zenith apresenta um mostrador cortado de um meteorito real, revelando os padrões de Widmanstätten naturais e únicos."
    }
]

@app.route('/')
def index():
    # Passamos apenas os 3 primeiros para a Home
    return render_template('index.html', relogios=RELOGIOS[:3])

@app.route('/colecao')
def colecao():
    # Passamos a lista completa para a página de coleção
    return render_template('colecao.html', relogios=RELOGIOS)

@app.route('/produto/<int:id>')
def produto(id):
    # Rota dinâmica para detalhes do produto
    if 0 <= id < len(RELOGIOS):
        rel = RELOGIOS[id]
        return render_template('produto.html', rel=rel)
    return "Produto não encontrado", 404

if __name__ == '__main__':
    app.run(debug=True)