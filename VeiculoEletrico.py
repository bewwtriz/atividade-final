import sqlite3

def criar_banco():
    conn = sqlite3.connect('estacaoCarregamento_db.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS registro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            placa TEXT NOT NULL,
            modelo TEXT NOT NULL,
            status TEXT NOT NULL,
            tempo_carregamento REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

criar_banco()

class VeiculoEletrico:
    def __init__(self):
        self.conn = sqlite3.connect('estacaoCarregamento_db.db')
        self.c = self.conn.cursor()

    def cadastrarVeiculo(self, placa, modelo, tempo_carregamento):
        try:
            self.c.execute('''
                INSERT INTO registro (placa, modelo, status, tempo_carregamento)
                VALUES (?, ?, ?, ?)
            ''', (placa, modelo, "Disponível", tempo_carregamento))
            self.conn.commit()
            print("Veículo cadastrado com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao cadastrar veículo: {e}")

    def consultarVeiculos(self):
        self.c.execute('SELECT * FROM registro')
        veiculos = self.c.fetchall()
        if not veiculos:
            print("Nenhum veículo cadastrado.")
        for veiculo in veiculos:
            print(f"ID: {veiculo[0]}, Placa: {veiculo[1]}, Modelo: {veiculo[2]}, Status: {veiculo[3]}, Tempo de Carregamento: {veiculo[4]} horas")

    def iniciarCarregamento(self, id):
        self.c.execute('SELECT status FROM registro WHERE id = ?', (id,))
        status = self.c.fetchone()
        if status and status[0] == "Disponível":
            self.c.execute('UPDATE registro SET status = ? WHERE id = ?', ("Em Carregamento", id))
            self.conn.commit()
            print("Veículo em carregamento")
        else:
            print("Veículo não está disponível para carregamento.")

    def finalizarCarregamento(self, id, custo):
        self.c.execute('SELECT modelo, tempo_carregamento, status FROM registro WHERE id = ?', (id,))
        resultado = self.c.fetchone()
        if resultado and resultado[2] == "Em Carregamento":
            tempo = resultado[1]
            total_custo = custo * tempo
            self.c.execute('UPDATE registro SET status = ? WHERE id = ?', ("Carregamento Finalizado", id))
            self.conn.commit()
            print(f"Modelo do veículo: {resultado[0]}; Custo: {total_custo:.2f}")
        else:
            print("Veículo não pode ter o carregamento finalizado ainda.")

    def consultarStatus(self, id):
        self.c.execute('SELECT * FROM registro WHERE id = ?', (id,))
        veiculo = self.c.fetchone()
        if veiculo:
            print(f"ID: {veiculo[0]}, Placa: {veiculo[1]}, Modelo: {veiculo[2]}, Status: {veiculo[3]}, Tempo de Carregamento: {veiculo[4]} horas")
        else:
            print("Veículo não encontrado.")

    def deletarVeiculo(self, id):
        self.c.execute('DELETE FROM registro WHERE id = ?', (id,))
        if self.c.rowcount > 0:
            self.conn.commit()
            print("Veículo removido com sucesso!")
        else:
            print("Veículo não encontrado ou já foi excluído.")

    def close(self):
        self.conn.close()

