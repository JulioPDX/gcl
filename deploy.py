#!/usr/bin/env python

"""Script used to configure the network"""

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_configure
from tools import nornir_set_creds


def deploy_network(task):
    """Configures network with Scrapli"""
    if "client" in task.host.name:
        pass
    else:
        task1_result = task.run(
            name=f"Configuring {task.host.name}!",
            task=napalm_configure,
            filename=f"configs/post/{task.host.name}.cfg",
            replace=True,
        )


def main():
    """Used to run all the things"""
    norn = InitNornir(config_file="nornir_settings/config.yaml")
    nornir_set_creds(norn)
    result = norn.run(task=deploy_network)
    print_result(result)


if __name__ == "__main__":
    main()
