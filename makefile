PYTHON = python3
APP_FILE = app.py
VAR_FILE = var.py
PDFREACTOR_FILE = PDFreactor.py
SHELL_FILE = shell

all: $(SHELL_FILE)

$(SHELL_FILE): $(APP_FILE) $(VAR_FILE) $(PDFREACTOR_FILE)
	$(PYTHON) $(APP_FILE) > $(SHELL_FILE)

clean:
	rm -f $(SHELL_FILE)
