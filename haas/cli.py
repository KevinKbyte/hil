"""This module implements the HaaS command line tool."""
from haas import config
from haas.config import cfg

import logging
import inspect
import sys
import urllib
import requests

commands = {}


def cmd(f):
    """A decorator, which resgisters it's argument as a command."""
    commands[f.__name__] = f
    return f


def check_status_code(response):
    if response.status_code < 200 or response.status_code >= 300:
        sys.stderr.write('Unexpected status code: %d\n' % response.status_code)
        sys.stderr.write('Response text:\n')
    sys.stderr.write(response.text)

# TODO: This function's name is no longer very accurate.  As soon as it is
# safe, we should change it to something more generic.
def object_url(*args):
    url = cfg.get('client', 'endpoint')
    for arg in args:
        url += '/' + urllib.quote(arg)
    return url


@cmd
def serve():
    """Start the HaaS API server"""
    from haas import model, api
    model.init_db()
    api.app.run(debug=True)

@cmd
def init_db():
    """Initialize the database"""
    from haas import model
    model.init_db(create=True)

@cmd
def user_create(username, password):
    """Create a user <username> with password <password>."""
    url = object_url('user', username)
    check_status_code(requests.put(url, data={'password': password}))

@cmd
def network_create(network, project):
    """Create a <network> belonging to a <project>"""
    url = object_url('network', network)
    check_status_code(requests.put(url, data={'project': project}))

@cmd
def network_delete(network):
    """Delete a <network>"""
    url = object_url('network', network)
    check_status_code(requests.delete(url))

@cmd
def user_delete(username):
    """Delete the user <username>"""
    url = object_url('user', username)
    check_status_code(requests.delete(url))

@cmd
def group_add_user(group, user):
    """Add <user> to <group>"""
    url = object_url('group', group, 'add_user')
    check_status_code(requests.post(url, data={'user': user}))

@cmd
def group_remove_user(group, user):
    """Remove <user> from <group>"""
    url = object_url('group', group, 'remove_user')
    check_status_code(requests.post(url, data={'user': user}))

@cmd
def project_create(project, group):
    """Create <project> belonging to <group>"""
    url = object_url('project', project)
    check_status_code(requests.put(url, data={'group': group}))

@cmd
def project_delete(project):
    """Delete <project>"""
    url = object_url('project', project)
    check_status_code(requests.delete(url))

@cmd
def group_create(group):
    """Create <group>"""
    url = object_url('group', group)
    check_status_code(requests.put(url))

@cmd
def group_delete(group):
    """Delete <group>"""
    url = object_url('group', group)
    check_status_code(requests.delete(url))

@cmd
def project_deploy(project):
    """Apply the networking of a <project>"""
    url = object_url('project', project, 'deploy')
    check_status_code(requests.post(url))

@cmd
def headnode_create(headnode, project):
    """Create a <headnode> belonging to <project>"""
    url = object_url('headnode', headnode)
    check_status_code(requests.put(url, data={'project': project}))

@cmd
def headnode_delete(headnode):
    """Delete <headnode>"""
    url = object_url('headnode', headnode)
    check_status_code(requests.delete(url))

@cmd
def project_connect_node(project, node):
    """Connect <node> to <project>"""
    url = object_url('project', project, 'connect_node')
    check_status_code(requests.post(url, data={'node': node}))

@cmd
def project_detach_node(project, node):
    """Detach <node> from <project>"""
    url = object_url('project', project, 'detach_node')
    check_status_code(requests.post(url, data={'node': node}))

@cmd
def node_register(node):
    """Register a node named <node>"""
    url = object_url('node', node)
    check_status_code(requests.put(url))

@cmd
def node_register_nic(node, nic, macaddr):
    """Register existence of a <nic> with the given <macaddr> on the given <node>"""
    url = object_url('node', node, 'nic', nic)
    check_status_code(requests.put(url, data={'macaddr':macaddr}))

@cmd
def node_delete_nic(node, nic):
    """Delete a <nic> on a <node>"""
    url = object_url('node', node, 'nic', nic)
    check_status_code(requests.delete(url))

@cmd
def headnode_create_hnic(headnode, nic, macaddr):
    """Create a <nic> with the given <macaddr> on the given <headnode>"""
    url = object_url('headnode', headnode, 'hnic', nic)
    check_status_code(requests.put(url, data={'macaddr':macaddr}))

@cmd
def headnode_delete_hnic(headnode, nic):
    """Delete a <nic> on a <headnode>"""
    url = object_url('headnode', headnode, 'hnic', nic)
    check_status_code(requests.delete(url))

@cmd
def node_connect_network(node, nic, network):
    """Connect <node> to <network> on given <nic>"""
    url = object_url('node', node, 'nic', nic, 'connect_network')
    check_status_code(requests.post(url, data={'network':network}))

@cmd
def node_detach_network(node, nic):
    """Detach <node> from the network on given <nic>"""
    url = object_url('node', node, 'nic', nic, 'detach_network')
    check_status_code(requests.post(url))

@cmd
def headnode_connect_network(headnode, nic, network):
    """Connect <headnode> to <network> on given <nic>"""
    url = object_url('headnode', headnode, 'hnic', nic, 'connect_network')
    check_status_code(requests.post(url, data={'network':network}))

@cmd
def headnode_detach_network(headnode, nic):
    """Detach <headnode> from the network on given <nic>"""
    url = object_url('headnode', headnode, 'hnic', hnic, 'detach_network')
    check_status_code(requests.post(url))

@cmd
def switch_register(name, driver):
    """Register a switch using driver <driver> under the name <name>"""
    url = object_url('switch', name)
    check_status_code(requests.put(url, data={'driver': driver}))

@cmd
def switch_delete(name):
    """Delete the switch named <name>"""
    url = object_url('switch', name)
    check_status_code(requests.delete(url))

@cmd
def port_register(switch, port):
    """Register a <port> on a <switch>"""
    url = object_url('switch', switch, 'port', port)
    check_status_code(requests.put(url))

@cmd
def port_delete(switch, port):
    """Delete a <port> on a <switch>"""
    url = object_url('switch', switch, 'port', port)
    check_status_code(requests.delete(url))

@cmd
def port_connect_nic(switch, port, node, nic):
    """Connect a <port> on a <switch> to a <nic> on a <node>"""
    url = object_url('switch', switch, 'port', port, 'connect_nic')
    check_status_code(requests.post(url, data={'node': node, 'nic': nic}))

@cmd
def port_detach_nic(switch, port):
    """Detach a <port> on a <switch> from whatever's connected to it"""
    url = object_url('switch', switch, 'port', port, 'detach_nic')
    check_status_code(requests.post(url))

@cmd
def list_free_nodes():
    """List all free nodes"""
    url = object_url('free_nodes')
    check_status_code(requests.get(url))

@cmd
def show_node(node):
    """Display information about a <node>"""
    url = object_url('node', node)
    check_status_code(requests.get(url))


@cmd
def help(*command_list):
    """Display usage of all following commands, or of all commands if none are given"""
    # FIXME: Displaying help for help doesn't work well with our function
    # inspection, because we don't handle variable lists right now.
    if not command_list:
        sys.stderr.write('Usage: %s <command> [<arguments>]... \n\n' % sys.argv[0])
        sys.stderr.write('Where <command> is one of:\n\n')
        command_list = sorted(commands.keys())
    for name in command_list:
        # For each command, print out a summary including the name, arguments,
        # and the docstring (as a #comment).
        func = commands[name]
        args, _, _, _ = inspect.getargspec(func)
        args = map(lambda name: '<%s>' % name, args)
        sys.stderr.write('  %s %s\n      %s\n' % (name, ' '.join(args), func.__doc__))


def main():
    """Entry point to the CLI.

    There is a script located at ${source_tree}/scripts/haas, which invokes
    this function.
    """
    logging.basicConfig(level=logging.DEBUG)
    config.load()
    if len(sys.argv) < 2 or sys.argv[1] not in commands:
        # Display usage for all commands
        help()
    else:
        commands[sys.argv[1]](*sys.argv[2:])

