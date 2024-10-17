#Note %%{gem_name} is is derived from the back part of %%{name} 
#Doc and debug packages are automatically created as required.

Summary:    Simple ruby build program with capabilities similar to make
Name:       rubygem-rake
Version:    13.0.6
Release:    2
License:    MIT
Group:      Development/Ruby
URL:        https://rake.rubyforge.org/
Source0:    http://rubygems.org/downloads/rake-%{version}.gem
BuildArch:  noarch
BuildRequires: rubygems
BuildRequires: p7zip

%description
This package contains Rake, a simple ruby build program with capabilities
similar to make.

%prep
%autosetup -p1 -n %{gem_name}-%{version}

%build
%gem_build

%install
%gem_install

%files
%{_bindir}/rake
%{gem_files}