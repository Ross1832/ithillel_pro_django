
def qs2html(sq_list):
    s = '<table>'
    for record in sq_list:
        s += f'<tr><td>{record.first_name}</td>' \
             f'<td>{record.last_name}</td>' \
             f'<td>{record.email}</td></tr>'
    s += '</table>'

    return s
