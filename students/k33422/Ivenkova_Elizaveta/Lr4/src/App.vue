<template>
  <div style="color: white">
    <b-navbar toggleable="lg" variant="dark">
      <h3 style="margin-right: 20px;">ELibrary </h3>
      <b-navbar-toggle target="nav-collapse" ></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-dropdown text="Reader" variant="dark" right>
            <div style="display: flex; flex-direction: column">
              <b-button @click="navigateTo('/reader/rare_books')">With rare Books</b-button>
              <b-button @click="navigateTo('/reader/outdated')">With outdated</b-button>
              <b-button @click="navigateTo('/reader/book_month_ago')">Book a Month Ago</b-button>
              <b-button @click="navigateTo('/reader/create')">Create Reader</b-button>
              <b-button @click="navigateTo('/reader/add_book')">Add Book</b-button>
            </div>
          </b-dropdown>

          <!-- Book Instances Button -->
          <b-button variant="dark" @click="navigateTo('/book_instance/list')">Book Instances</b-button>

          <!-- Statistics Button -->
          <b-button variant="dark" @click="navigateTo('/statistics')">Statistics</b-button>

          <!-- User Dropdown -->
          <b-dropdown text="User" variant="dark" right>
            <div style="display: flex; flex-direction: column">
            <b-button @click="navigateTo('/user/login')">User Login</b-button>
            <b-button @click="navigateTo('/user/update')">User Update</b-button>
            <b-button @click="navigateTo('/user/registration')">User Registration</b-button>
            </div>
          </b-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
  <router-view></router-view>
</template>

<script setup>
import { BNavbar, BNavbarBrand, BNavbarNav, BNavbarToggle, BCollapse, BNavItemDropdown, BDropdownItem } from 'bootstrap-vue-3'
import { useRouter } from 'vue-router';
const router = useRouter();

function navigateTo(path) {
  router.push(path);
}
</script>

  <style scoped>
  body {
    margin: 0;
    padding: 0;
  }

  .navbar {
    margin-bottom: 0;
  }
</style>

