from server_errors import OK, NotFound, ServerError


if __name__ == "__main__":
    ok_error = OK()
    not_found_error = NotFound()
    server_error = ServerError()

    ok_error.status()
    not_found_error.status()
    server_error.status()
