variable "gcp_sakey" {}
variable "gce_project" {}
variable "gce_region" {}
variable "gce_zone" {}
variable "gce_ssh_user" {}
variable "gce_ssh_pub_key_file" {}

// https://www.terraform.io/docs/providers/google/index.html
provider "google" {
  credentials = file(var.gcp_sakey)
  project     = var.gce_project
  region      = var.gce_region
}

// https://www.terraform.io/docs/providers/google/r/compute_firewall.html
resource "google_compute_firewall" "web-0" {
  name        = "web-0"
  network     = "default"
  target_tags = ["web"]

  allow {
    protocol = "udp"
    ports    = ["443"]
  }

  allow {
    protocol = "tcp"
    ports    = ["80", "443"]
  }
}

// https://www.terraform.io/docs/providers/google/d/datasource_compute_address.html
resource "google_compute_address" "web-0" {
  name = "web-0"
}

// https://www.terraform.io/docs/providers/google/d/datasource_compute_instance.html
resource "google_compute_instance" "web-0" {
  name         = "web-0"
  machine_type = "g1-small"
  zone         = var.gce_zone
  tags         = ["web"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }

  metadata = {
    ssh-keys = "${var.gce_ssh_user}:${var.gce_ssh_pub_key_file}"
  }

  network_interface {
    network = "default"

    access_config {
      nat_ip = google_compute_address.web-0.address
    }
  }
}

output "ip" {
  value = google_compute_instance.web-0.network_interface.0.access_config.0.nat_ip
}
