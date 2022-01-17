DASHBOARDS_DIR := dashboards-to-provision
DASHBOARDS_GENS := $(shell find $(DASHBOARDS_DIR) -name '*.dashboard.py')
DASHBOARDS := $(DASHBOARDS_GENS:.dashboard.py=.json)

.PHONY: all
all: $(DASHBOARDS)

venv/bin/activate:
	python3 -m venv venv

venv/.requirements-installed: requirements.txt venv/bin/activate
	. venv/bin/activate && \
		pip3 install -r $<
	touch $@

%.json: %.dashboard.py dashboards-to-provision/common.py venv/.requirements-installed
	. venv/bin/activate && \
		PYTHONPATH=$(DASHBOARDS_DIR):$$PYTHONPATH generate-dashboard -o $@ $<
