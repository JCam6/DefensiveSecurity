# run with sudo
# make sure python3 is installed

import os


def main():
    # Print header for program.
    print('\n', '*' * 10, 'Starting The Program', '*' * 10, '\n')

    # Install Docker.
    install_request = input("\n>>> Install Docker? Type y or n, then hit enter:  ")
    if install_request == "y":
        os.system("apt-get update")
	os.system("apt-get install apt-transport-https ca-certificates curl gnupg lsb-release")
	os.system("curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg")
	os.system("echo \
  		"deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  		$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null")
	os.system("apt-get update")
	os.system("apt-get install docker-ce docker-ce-cli containerd.io")
	os.system("docker run --help")
    else:
        print("\n>>> OK")


main()
