terraform {
  required_version = ">= 1.8"
}

variable "name" {
  description = "Logical name for the synthetic reference environment."
  type        = string
  default     = "hyperion-example"

  validation {
    condition     = can(regex("^[a-z0-9][a-z0-9-]{1,62}$", var.name))
    error_message = "name must be a lowercase DNS-style label."
  }
}

variable "cluster_cidr" {
  type    = string
  default = "10.42.0.0/16"
}

variable "service_cidr" {
  type    = string
  default = "10.43.0.0/16"
}

resource "terraform_data" "reference" {
  input = {
    name         = var.name
    cluster_cidr = var.cluster_cidr
    service_cidr = var.service_cidr
  }
}

output "environment" {
  value = terraform_data.reference.output
}
