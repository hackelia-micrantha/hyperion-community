terraform {
  required_version = ">= 1.8.0"

  required_providers {
    incus = {
      source  = "lxc/incus"
      version = "~> 0.4"
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
}
