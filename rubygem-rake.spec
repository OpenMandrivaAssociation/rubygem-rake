#Note %%{gem_name} is is derived from the back part of %%{name} 
#Doc and debug packages are automatically created as required.

Summary:    Simple ruby build program with capabilities similar to make
Name:       rubygem-rake
Version:    13.0.6
Release:    2
License:    MIT
Group:      Development/Ruby
URL:        http://rake.rubyforge.org/
Source0:    http://rubygems.org/downloads/%{gem_name}-%{version}.gem
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

# Install manpage
##mkdir -p %%{buildroot}%%{_mandir}/man1/
# use 7z and not gzip, as the file is corrupted.
# For some reason it works fine with 7z.
#7z e doc/%%{gem_name}.1.gz 
#install %%{gem_name}.1 %%{buildroot}%%{_mandir}/man1/rake.1

%files
%{_bindir}/rake
#%%{_mandir}/man1/*
%{gem_files}