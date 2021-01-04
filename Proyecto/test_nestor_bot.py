from nestor_bot import NestorBot

#Para lectura
def test_read_sql():
    nestor = NestorBot("#channel")
    result = nestor.get_message_payload("show columns from mensaje")
    columns = ["idmensaje","contenido","data","idusuario","idcanal"]
    assert result['channel'] == "#channel"
    for i in range(5):
        assert result['blocks'][0][i][0] == columns[i]

#Para insertar
def test_write_sql():
    nestor = NestorBot("#channel")
    result = nestor.get_message_payload("insert into usuario(nombreusuario) values('usuarioTest')")
    assert result['blocks'][0] == "OK +"