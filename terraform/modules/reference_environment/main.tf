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
  description = "Synthetic pod network used only by the reference contract."
  type        = string
  default     = "192.0.2.0/24"

  validation {
    condition     = can(cidrnetmask(var.cluster_cidr))
    error_message = "cluster_cidr must be valid CIDR notation."
  }
}

variable "service_cidr" {
  description = "Synthetic service network used only by the reference contract."
  type        = string
  default     = "198.51.100.0/24"

  validation {
    condition     = can(cidrnetmask(var.service_cidr))
    error_message = "service_cidr must be valid CIDR notation."
  }
}

resource "terraform_data" "reference" {
  input = {
    name         = var.name
    cluster_cidr = var.cluster_cidr
    service_cidr = var.service_cidr
  }
}

output "environment" {
  description = "Synthetic, non-deploying reference environment contract."
  value       = terraform_data.reference.output
}