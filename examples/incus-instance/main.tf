terraform {
  required_version = ">= 1.8.0"

  required_providers {
    incus = {
      source  = "lxc/incus"
      version = "~> 1.0"
    }
  }
}

provider "incus" {}

module "reference_instance" {
  source = "../../terraform/modules/incus_instance"

  name  = "hyperion-community-reference"
  image = "images:debian/12"

  config = {
    "limits.cpu"    = "1"
    "limits.memory" = "1GiB"
  }

  # Synthetic device names are map keys, not fields inside the objects.
  devices = {
    root = {
      type = "disk"
      properties = {
        path = "/"
        pool = "example-pool"
      }
    }
    eth0 = {
      type = "nic"
      properties = {
        network = "example-network"
      }
    }
  }
}
